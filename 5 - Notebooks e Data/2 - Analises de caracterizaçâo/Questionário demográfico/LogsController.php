<?php
 
namespace console\controllers;
 
use yii\console\Controller;
use common\models\User;
use common\models\AlunosTurma;
use common\models\Turma;
use common\models\Trabalho;
use common\models\CodigoFonte;
use common\models\Submissao;
use common\models\UserQuestionario;
use common\models\Session;
use common\models\Log;
use common\models\ExercicioTrabalho;
use common\models\CacheNotas;
use DateTime;
 
/**
 * Clean controller
 */
class LogsController extends Controller {

    public $path = 'codes/logs/';
    public $rootpath = 'codes/';
    public $pathtemp = '/tmp/exec/';
    public $ipc_classes;
    public $folder_notas = 'scripts/data/notas/';
    public $notas = [];

    public $newpath;
    public $userspath;
    public $workspath;   
    public $classpath;
 
    public function actionComplete($ano, $semestre, $mouselogs = 0) {

        $folder_notas = $this->folder_notas . $ano ."-". $semestre;
        $files = scandir($folder_notas);

        foreach($files as $key => $value) {

            $path = realpath($folder_notas . DIRECTORY_SEPARATOR . $value);

            if (!is_dir($path)) {

                $csvfile = fopen($path,"r");
                
                while (($data = fgetcsv($csvfile, 1000, ";")) !== FALSE) {

                    if (array_key_exists(3, $data) && is_numeric($data[3])) {

                        $user = User::find()
                            ->where(['matricula' => $data[3]])
                            ->one();

                        if ($user) {

                            if (array_key_exists($data[3], $this->notas)) {
                                echo "ERRO: Aluno " . $data[3] . " já cadastrado! ";
                                echo $this->notas[$data[3]] . " -> " . $data[23] . "\n";
                            } 

                            $this->notas[$user->id] = $data[23];
                        }                        
                    } 
                }
            }
        }

        $total_turmas = [];
        $total_students = [];
        $homework_exercises = [];
        $exam_exercises = [];
        $total_codes = [];
        $total_executions = [];        

        if (($ano == 2016) and ($semestre == 1)) {
            $this->ipc_classes = "(102,103,105,106,107,108,109,110,111)";
        }        
        elseif (($ano == 2016) and ($semestre == 2)) {
            $this->ipc_classes = "(122,124,125,127,128)";
        }    
        else if (($ano == 2017) and ($semestre == 1)) {
            $this->ipc_classes = "(135,136,137,138,139,140,141,142,143,144)";
        }
        elseif (($ano == 2017) and ($semestre == 2)) {
            $this->ipc_classes = "(160,162,163,164,165)";
        }
        elseif (($ano == 2018) and ($semestre == 1)) {
            $this->ipc_classes = "(180,181,183,185,186,187,188,189,190)";
        }        
        elseif (($ano == 2018) and ($semestre == 2)) {
            $this->ipc_classes = "(204,205,206,207,208)";
        }                
        elseif (($ano == 2019) and ($semestre == 1)) {
            $this->ipc_classes = "(220,221,222,223,224,225,226,230,231)";
        }          
        elseif (($ano == 2019) and ($semestre == 2)) {
            $this->ipc_classes = "(258,259,260,261,262,263,264)";
        }           

        $this->newpath = 'codes/dataset/'.$ano.'-'.$semestre.'/';

        if (!is_dir($this->newpath)) {
            mkdir($this->newpath);
        }             

        if (!is_dir($this->pathtemp)) {
            mkdir($this->pathtemp);
        }                    

        $turmas = Turma::find()
            ->where('id IN ' . $this->ipc_classes)
            ->andWhere('numero_turma NOT LIKE "%teste%"')
            ->andWhere(['status' => Turma::STATUS_ACTIVE])
            ->all();

        foreach ($turmas as $turma) {

            $this->classpath = $this->newpath . $turma->id . '/';
            $soma_ponderada_avaliacoes = array_fill(0, 10000, 0);
            $soma_pesos_avaliacoes = 0;
            $soma_ponderada_listas = array_fill(0, 10000, 0);
            $nomes_alunos = [];
            $soma_pesos_listas = 0;
            $prova_final = [];

            $professor_e_monitores = [$turma->professor->id];

            foreach ($turma->monitores as $monitor) {
                $professor_e_monitores[] = $monitor->id;
            }            

            if (!is_dir($this->classpath)) {
                mkdir($this->classpath);
            } 

            $this->userspath = $this->classpath . 'users/';
            $this->workspath = $this->classpath . 'assessments/';        
                
            $trabalhos = Trabalho::find() 
                ->where(['id_turma' => $turma->id])
                ->andWhere(['status' => Trabalho::STATUS_ACTIVE])
                ->orderBy('id ASC')
                ->all();

            $total_turmas['turma_' . $turma->id] = 1;

            foreach ($trabalhos as $trabalho) {
                
                if ($trabalho->tipo == 2) {
                    $soma_pesos_avaliacoes = $soma_pesos_avaliacoes + $trabalho->peso;
                } else {
                    $soma_pesos_listas = $soma_pesos_listas + $trabalho->peso;
                }

                if (!is_dir($this->workspath)) {
                    mkdir($this->workspath);
                }                        

                $data  = "-- ASSESSMENT DATA:\n";
                $data .= "---- assessment title: " . $trabalho->titulo . "\n";
                $data .= "---- class name: " . $trabalho->turma->disciplina->nome . "\n";
                $data .= "---- class number: " . $trabalho->turma->id . "\n";

                list($dia, $mes, $ano, $hor, $min) = sscanf($trabalho->inicio, '%d/%d/%d %d:%d');
                $inicio = $ano."-".sprintf("%02d", $mes)."-".sprintf("%02d", $dia)." ".sprintf("%02d", $hor).":".sprintf("%02d", $min);                                
                $data  .= "---- start: " . $inicio . "\n";

                list($dia, $mes, $ano, $hor, $min) = sscanf($trabalho->termino, '%d/%d/%d %d:%d');
                $termino = $ano."-".sprintf("%02d", $mes)."-".sprintf("%02d", $dia)." ".sprintf("%02d", $hor).":".sprintf("%02d", $min);                                                
                $data .= "---- end: " . $termino . "\n";

                $data .= "---- language: " . $trabalho->linguagem->nome . "\n";
                $data .= "---- codemirror mode: " . $trabalho->linguagem->mode_codemirror . "\n";
                $data .= "---- type: ";
                $data .= ($trabalho->tipo==1)?"homework\n":"exam\n";
                $data .= "---- weight: " . $trabalho->peso . "\n";

                $exercicios = ExercicioTrabalho::find()
                    ->where(['id_trabalho' => $trabalho->id])
                    ->orderBy('bloco_aleatorio ASC')
                    ->all();

                $data .= "---- total_exercises: " . count($exercicios) . "\n";

                $data .= "-- EXERCISES:\n";

                foreach ($exercicios as $exec) {

                    if ($trabalho->tipo == 1) {
                        $homework_exercises['ex_' . $exec->id] = 1;
                    } else {
                        $exam_exercises['ex_' . $exec->id] = 1;
                    }

                    $data .= "---- exercise ".sprintf("%02d", $exec->bloco_aleatorio).": " . str_replace(',', ' or ', $exec->exercicios) . "\n";
                }

                file_put_contents($this->workspath ."/". $trabalho->id . ".data", $data);

                $codigos_fonte = CodigoFonte::find()
                    ->where(['id_trabalho' => $trabalho->id])
                    ->orderBy('id ASC')
                    ->all();

                foreach ($codigos_fonte as $codigo_fonte) {

                    //print "=====> " . $codigo_fonte->id_aluno . " " . $codigo_fonte->id_trabalho . " " . $codigo_fonte->id_exercicio . " <=====\n";
                    $user = User::find()
                        ->where(['id' => $codigo_fonte->id_aluno])
                        ->orderBy('id ASC')
                        ->one();

                    $nomes_alunos[$codigo_fonte->id_aluno] = $user->username;

                    // O usuário precisa ser um aluno
                    if ($user->id_tipo != 4) {
                        continue;
                    }

                    if (in_array($user->id, $professor_e_monitores)) {
                        continue;
                    }

                    // Diretório do logs dos alunos    
                    if (!is_dir($this->userspath)) {
                        mkdir($this->userspath);
                    }     

                    // Diretório do logs do aluno
                    if (!is_dir($this->userspath . $codigo_fonte->id_aluno)) {
                        mkdir($this->userspath . $codigo_fonte->id_aluno);
                    }                       
                    
                    // Diretório do mouse moves
                    if ($mouselogs == 1) {
                    
                        if (!is_dir($this->userspath . $codigo_fonte->id_aluno . "/mousemove/")) {
                            mkdir($this->userspath . $codigo_fonte->id_aluno . "/mousemove/");
                        }

                        $orig = $this->rootpath . $codigo_fonte->id_aluno . '/' . $trabalho->id . '/mousemove.txt';    
                        $dest = $this->userspath . $codigo_fonte->id_aluno . "/mousemove/" . $trabalho->id . ".data";

                        if (!file_exists($dest) && file_exists($orig)) {
                            copy ($orig, $dest);
                        }         

                    }                                
                    
                    $total_students['student_' . $codigo_fonte->id_aluno] = 1;
                    $total_codes['code_'. $codigo_fonte->id] = 1;

                    // Diretório do logs do aluno
                    if (!is_dir($this->userspath . $codigo_fonte->id_aluno . "/executions/")) {
                        mkdir($this->userspath . $codigo_fonte->id_aluno . "/executions/");
                    }   

                    // Diretório do logs do aluno
                    if (!is_dir($this->userspath . $codigo_fonte->id_aluno . "/codes/")) {
                        mkdir($this->userspath . $codigo_fonte->id_aluno . "/codes/");
                    }                       
                    
                    // Submissoes
                    $submissoes = Submissao::find()
                        ->where(['id_codigo_fonte' => $codigo_fonte->id])
                        ->orderBy('id ASC')
                        ->all();

                    $data = "";

                    foreach ($submissoes as $sub) {

                        $total_executions['ex_' . $sub->id] = 1;       

                        $data .= "== ";
                        $data .= ($sub->tipo==1)?"TEST":"SUBMITION";
                        $data .= " (" . $sub->data_hora . ") \n";
                        $data .= "-- CODE:\n";                        
                        $data .= $sub->codigo . "\n";

                        if ($sub->tipo==1) {

                            // Checo se existe um erro para esse codigo já gravado no banco
                            if ($sub->dataset) {
                                if (!empty($sub->executavel_erro)) {
                                    $executavel_erro = $sub->executavel_erro;
                                    $executavel_saida = "";
                                    //echo "Peguei erro\n";
                                } 
                                // Checo se existe uma saida para esse codigo já gravada no banco
                                elseif (!empty($sub->executavel_saida)) {
                                    $executavel_saida = $sub->executavel_saida;
                                    $executavel_erro = "";
                                    //echo "Peguei saida\n";
                                }    
                            }
                            // Se não, executo o código e gravo a saida ou o erro no banco
                            else {

                                // Lendo os parametros e removendo espaços adicionais e novas linhas
                                $parametros = $sub->codigoFonte->exercicio->correcao_entrada;            
                                $parametros = trim($parametros);
                
                                if ($trabalho->linguagem->tipo_entrada == 'file') {
                
                                    $parametros = preg_replace('/(?:\s\s+|\s|\t)/', "\n", $parametros);
                                    file_put_contents ($this->pathtemp . 'cbtemp.txt', $parametros);
                                    file_put_contents ($this->pathtemp . 'code' . $trabalho->linguagem->extensao, $this->deletaLinhas($trabalho, $sub->codigo));
                
                                    $comando_execucao = "timeout 3 python3 " . $this->pathtemp . 'code' . $trabalho->linguagem->extensao;
                                    $comando_execucao = $comando_execucao . ' < '. $this->pathtemp . 'cbtemp.txt';
                
                                    $process = proc_open($comando_execucao, array(
                                        1 => array("pipe", "w"),  // stdout
                                        2 => array("pipe", "w")   // stderr
                                    ), $pipes);
                
                                    $executavel_saida = stream_get_contents($pipes[1]);
                                    $executavel_erro = str_replace($this->pathtemp . 'code' . $trabalho->linguagem->extensao, "XXXX", stream_get_contents($pipes[2]));

                                    if ($executavel_erro) {
                                        $sub->executavel_erro = trim(substr($executavel_erro,0,1000));
                                    } 
                                    elseif ($executavel_saida) {
                                        $sub->executavel_saida = trim(substr($executavel_saida,0,1000));
                                    }

                                    $sub->dataset = 1;
                                    $sub->save();
                                    //echo "salvei ".$sub->id."!\n";                                    

                                }
                            }

                            if ($executavel_saida) {
                                $data .= "-- OUTPUT:\n";
                                $data .= trim(substr($executavel_saida,0,1000)) . "\n";
                            }
                            if ($executavel_erro) {
                                $executavel_erro = str_replace($this->pathtemp . 'code' . $trabalho->linguagem->extensao, "XXXX", $executavel_erro);
                                $data .= "-- ERROR:\n";
                                $data .= $executavel_erro . "\n";
                            }

                        }

                        if ($sub->tipo==2) {

                            $data .= "-- EXECUTION TIME:\n";
                            $data .= $sub->tempo_execucao_ms . "\n";                                
                            if (!empty($sub->executavel_erro)) {
                                $data .= "-- ERROR:\n";
                                $data .= $sub->executavel_erro . "\n";                                   
                            } else {
                                $data .= "-- TEST CASE 1:\n";
                                $data .= "---- input:\n";
                                $data .= $codigo_fonte->exercicio->correcao_entrada . "\n";
                                $data .= "---- correct output:\n";
                                $data .= $codigo_fonte->exercicio->correcao_saida . "\n";
                                $data .= "---- user output:\n";
                                $data .= trim(substr($sub->executavel_saida,0,1000)) . "\n";   
                                if (!empty($codigo_fonte->exercicio->correcao_entrada_2)) {
                                    $data .= "-- TEST CASE 2:\n";
                                    $data .= "---- input:\n";
                                    $data .= $codigo_fonte->exercicio->correcao_entrada_2 . "\n";
                                    $data .= "---- correct output:\n";
                                    $data .= $codigo_fonte->exercicio->correcao_saida_2 . "\n";
                                    $data .= "---- user output:\n";
                                    $data .= trim(substr($sub->executavel_saida_2,0,1000)) . "\n"; 
                                }
                                if (!empty($codigo_fonte->exercicio->correcao_entrada_3)) {
                                    $data .= "-- TEST CASE 3:\n";
                                    $data .= "---- input:\n";
                                    $data .= $codigo_fonte->exercicio->correcao_entrada_3 . "\n";
                                    $data .= "---- correct output:\n";
                                    $data .= $codigo_fonte->exercicio->correcao_saida_3 . "\n";
                                    $data .= "---- user output:\n";
                                    $data .= trim(substr($sub->executavel_saida_3,0,1000)) . "\n"; 
                                }                                
                                $data .= "-- GRADE:\n";
                                $data .= ($sub->corretude * 100) . "%\n";                                 
                                
                            }
                        }
                        $data .= "*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n";
                    }

                    file_put_contents($this->userspath . $codigo_fonte->id_aluno . "/executions/".($trabalho->id ."_". $codigo_fonte->exercicio->id).".log", $data);
                    file_put_contents($this->userspath . $codigo_fonte->id_aluno . "/codes/".($trabalho->id ."_". $codigo_fonte->exercicio->id) . $trabalho->linguagem->extensao, $codigo_fonte->codigo);

                    if (!file_exists($this->userspath . $codigo_fonte->id_aluno . "/logins.log")) {

                        $logins_and_logouts = "";
                        $logs = Log::find()
                            ->where(['id_user' => $codigo_fonte->id_aluno])
                            ->andWhere('ocorrencia like "%user/log%"')
                            ->orderBy('id ASC')
                            ->all();
                        foreach ($logs as $log) {
                            $ocorrencia = explode(" ID",$log->ocorrencia)[0];
                            $ocorrencia = str_replace("Action: ", "", $ocorrencia);
                            $logins_and_logouts .=  $log->data_hora . "#" . $ocorrencia . "\n";
                        }
                        file_put_contents($this->userspath . $codigo_fonte->id_aluno . "/logins.log", $logins_and_logouts);
                    }    

                    // Notas em provas e trabalhos
                    if (!is_dir($this->userspath . $codigo_fonte->id_aluno . "/grades")) {
                        mkdir($this->userspath . $codigo_fonte->id_aluno . "/grades");
                    }     
                    
                    if (!file_exists($this->userspath . $codigo_fonte->id_aluno . "/grades/".$trabalho->id.".log")) {
                        $nota = CacheNotas::find()
                            ->where(['id_aluno' => $codigo_fonte->id_aluno])
                            ->andWhere(['id_trabalho' => $trabalho->id])
                            ->orderBy('id ASC')
                            ->one();
                        
                        if ($nota) {
                            $data  = "---- grade (0-10): " . $nota->nota . "\n";
                            $data .= "---- number of exercises: " . $nota->total_questoes . "\n";
                            $data .= "---- correct: " . $nota->total_acertos . "\n";
                            $data .= "---- incorrect: " . $nota->incorretas . "\n";                
                            $data .= "---- blank: " . $nota->nao_resolvidas;
                            file_put_contents($this->userspath . $codigo_fonte->id_aluno . "/grades/".$trabalho->id.".log", $data);    

                            if ($trabalho->tipo == 2) {
                                $soma_ponderada_avaliacoes[$codigo_fonte->id_aluno] += $nota->nota * $trabalho->peso;
                                if ($trabalho->peso == 0) {
                                    $prova_final[$codigo_fonte->id_aluno] = $nota->nota;
                                }
                            } else {
                                $soma_ponderada_listas[$codigo_fonte->id_aluno] += $nota->nota * $trabalho->peso;
                            }

                        }

                    }                    
                    
                    if (!file_exists($this->userspath . $codigo_fonte->id_aluno . "/user.data")) {

                        $questionario = UserQuestionario::find()
                            ->where(['id_user' => $codigo_fonte->id_aluno])
                            ->one();       

                        $data  = "-- CURRENT DEGREE COURSE: \n";
                        $data .= "---- course id: " . $user->id_curso . "\n";
                        $data .= "---- course name: " . $user->curso->nome . "\n";
                        $data .= "---- institution id: " . $user->curso->id_instituicao . "\n";
                        $data .= "---- institution name: " . $user->curso->instituicao->nome . "\n";                            
                            
                        if ($questionario) {
                            $data .= "-- HIGH SCHOOL: \n";
                            $data .= "---- high school name: " . $questionario->escola_em . "\n";
    
                            // TIPO DE ESCOLA: 1 => 'Pública convencional', 2 => 'Particular convencional', 3 => 'Técnica'
                            if ($questionario->tipo_escola_em == 1) {
                                $school_type = 'public school';
                            } 
                            elseif ($questionario->tipo_escola_em == 2) {
                                $school_type = 'private school';
                            }
                            elseif ($questionario->tipo_escola_em == 3) {
                                $school_type = 'technical school';
                            }                        
                            $data .= "---- school type: " . $school_type . "\n";
    
                            // TURNO: 1 => 'Matutino', 2 => 'Vespertino', 3 => 'Noturno', 4 => 'Integral'
                            if ($questionario->turno_em == 1) {
                                $turno_em = 'morning shift';
                            } 
                            elseif ($questionario->turno_em == 2) {
                                $turno_em = 'afternoon shift';
                            }
                            elseif ($questionario->turno_em == 3) {
                                $turno_em = 'night shift';
                            }
                            elseif ($questionario->turno_em == 4) {
                                $turno_em = 'full-time school';
                            }   
                            if (isset($turno_em)) {
                                $data .= "---- shift: " . $turno_em . "\n";
                            }
    
                            $data .= "---- graduation year: " . $questionario->ano_conclusao_em . "\n";
    
                            $data .= "-- PERSONAL COMPUTER: \n";
    
                            if ($questionario->computador_pessoal == 1) {
                                
                                $data .= "---- has a PC at home: yes\n";     
    
                                // ACESSO EXCLUSIVO: 1 =>'Sim, tenho acesso exclusivo.', 2 => 'Não, o computador também é usado por outras pessoas em minha casa.'
                                if ($questionario->computador_exclusivo==1) {
                                    $data .= "---- share this PC with other people at home: no\n";
                                } else {
                                    $data .= "---- share this PC with other people at home: yes\n";
                                }
    
                                // INTERNET: 1 => 'Sim, com qualidade boa ou razoável', 2 =>'Sim, mas a qualidade é péssima', 3 =>'Não'
                                if ($questionario->internet==1) {
                                    $internet = 'yes (high-speed Internet)';
                                } 
                                elseif ($questionario->internet==2) {
                                    $internet = 'yes (low-speed Internet)';
                                }
                                elseif ($questionario->internet==3) {
                                    $internet = 'no';
                                }                            
    
                                $data .= "---- this PC has access to Internet: " . $internet . "\n";
    
                            } else {
                                $data .= "---- has a PC at home: no\n";                            
                                $data .= "---- share this PC with other people at home: n/a\n";
                                $data .= "---- this PC has access to Internet: n/a\n";
                            }
    
                            //Linguagem: 1 => 'Nunca programei', 2 => 'C', 3 => 'C++', 4 => 'Python', 5 => 'Java', 6 => 'Scratch',7 => 'Outra'
                            if ($questionario->linguagens == "1") {
                                $data .= "---- previous experience of any computer language: no\n";    
                            } else {
                                $data .= "---- previous experience of any computer language: yes (";    
                                $questionario->linguagens = str_replace("2", "C", $questionario->linguagens);
                                $questionario->linguagens = str_replace("3", "C++", $questionario->linguagens);
                                $questionario->linguagens = str_replace("4", "Python", $questionario->linguagens);
                                $questionario->linguagens = str_replace("5", "Java", $questionario->linguagens);
                                $questionario->linguagens = str_replace("6", "Scratch", $questionario->linguagens);
                                $questionario->linguagens = str_replace("7", "Other", $questionario->linguagens);
                                $data .= $questionario->linguagens . ")\n";    
                            }
    
                            $data .= "-- WORK: \n";
    
                            // Trabalho: 1 => 'Sim', 2 => 'Não', 
                            if ($questionario->trabalho == 1) {
                                $data .= "---- worked or interned before the degree: yes\n";
                                $data .= "---- company name: " . $questionario->nome_empresa . "\n";
                                $data .= "---- year started working: " . $questionario->trabalho_ano_inicio . "\n";
                                $data .= "---- year stopped working: " . $questionario->trabalho_ano_fim . "\n";
                            } else {
                                $data .= "---- worked or interned before the degree: no\n";
                                $data .= "---- company name: n/a\n";
                                $data .= "---- year started working: n/a\n";
                                $data .= "---- year stopped working: n/a\n";                            
                            }
    
                            $data .= "-- PREVIOUS DEGREE: \n";
    
                            // Graduacao prévia: 1 => 'Sim', 2 => 'Não'
                            if ($questionario->graduacao_anterior == 1) {
                                $data .= "---- started other degree programmes: yes\n";
                                $data .= "---- degree course: " . $questionario->curso_graduacao_anterior . "\n";
                                $data .= "---- institution name: " . $questionario->universidade_graduacao_anterior . "\n";
                                $data .= "---- year started this degree: " . $questionario->inicio_graduacao . "\n";
                                $data .= "---- year stopped this degree: " . $questionario->termino_graduacao . "\n";                                   
                            } else {
                                $data .= "---- started other degree programmes: no\n";
                                $data .= "---- degree course: n/a\n";
                                $data .= "---- institution name: n/a\n";
                                $data .= "---- year started this degree: n/a\n";
                                $data .= "---- year stopped this degree: n/a\n";
                            }
                     
                            $data .= "-- OTHER INFORMATION: \n";
                            // Sexo: 1 => 'Masculino', 2 => 'Feminino'
                            if ($questionario->sexo != -1) {
                                if ($questionario->sexo==1) {
                                    $data .= "---- sex: male\n";
                                } else {
                                    $data .= "---- sex: female\n";                        
                                }
                            }
                            
                            if ($questionario->ano_nascimento != -1) {
                                $data .= "---- year of birth: " . $questionario->ano_nascimento . "\n";                        
                            }
    
                            // Estado civil: 1 => 'Solteiro(a)', 2 =>'Casado(a)', 3 =>'Viúvo(a)'
                            if ($questionario->estado_civil == 1) {
                                $estado_civil = "single";
                            } 
                            elseif ($questionario->estado_civil == 2) {
                                $estado_civil = "married";
                            } 
                            elseif ($questionario->estado_civil == 3) {
                                $estado_civil = "widower";
                            }                        
                            $data .= "---- civil status: " . $estado_civil . "\n";                        
    
                            // Possui filhos: 1 => 'Sim', 2 => 'Não'
                            if ($questionario->filhos==1) {
                                $data .= "---- have kids: yes\n";                        
                            } else {
                                $data .= "---- have kids: no\n";                        
                            }
                                
                        }

                        file_put_contents($this->userspath . $codigo_fonte->id_aluno . "/user.data", $data);
                    }                         

                    // Logs do Codemirror
                    if (!is_dir($this->userspath . $codigo_fonte->id_aluno . "/codemirror")) {
                        mkdir($this->userspath . $codigo_fonte->id_aluno . "/codemirror");
                    }                     

                    if (file_exists($this->path . $codigo_fonte->id_aluno . "/" . $codigo_fonte->id_trabalho . "_" . $codigo_fonte->id_exercicio . ".log")) {

                        // Diretório, arquivo e linhas do log a ser lido
                        $dir = $this->path . $codigo_fonte->id_aluno;
                        $file = $this->file_get_contents_utf8($dir . "/" . $codigo_fonte->id_trabalho . "_" . $codigo_fonte->id_exercicio . ".log");
                        $linhas = explode("\n",$file);

                        // $newlog conterá todas as linhas do log ajustado
                        $newlog = "";
                        $hora_anterior = 0;

                        foreach ($linhas as $linha) {

                            $linha = trim($linha);

                            $linha = str_replace(":viewportChange:", "#viewportChange#", $linha);
                            $linha = str_replace(":mousedown:", "#mousedown#", $linha);
                            $linha = str_replace(":change:", "#change#", $linha);
                            $linha = str_replace(":focus:", "#focus#", $linha);
                            $linha = str_replace(":blur:", "#blur#", $linha);
                            $linha = str_replace(":testar:", "#testar#", $linha);
                            $linha = str_replace(":console_testar:", "#console_testar#", $linha);
                            $linha = str_replace(":keyHandled:", "#keyHandled#", $linha);
                            $linha = str_replace(":gutterClick:", "#gutterClick#", $linha);
                            $linha = str_replace(":copy:", "#copy#", $linha);
                            $linha = str_replace(":dblclick:", "#dblclick#", $linha);
                            $linha = str_replace(":touchstart:", "#touchstart#", $linha);
                            $linha = str_replace(":contextmenu:", "#contextmenu#", $linha);
                            $linha = str_replace(":viewportChange:", "#viewportChange#", $linha);
                            $linha = str_replace(":console_submeter:", "#console_submeter#", $linha);
                            $linha = str_replace(":submeter:", "#submeter#", $linha);
                            $linha = str_replace(":comando_execucao:", "#comando_execucao#", $linha);

                            $linha = str_replace(":viewportChange:", "#viewportChange#", $linha);
                            $linha = str_replace(":mousedown", "#mousedown", $linha);
                            $linha = str_replace(":change", "#change", $linha);
                            $linha = str_replace(":focus", "#focus", $linha);
                            $linha = str_replace(":blur", "#blur", $linha);
                            $linha = str_replace(":testar", "#testar", $linha);
                            $linha = str_replace(":console_testar", "#console_testar", $linha);
                            $linha = str_replace(":keyHandled", "#keyHandled", $linha);
                            $linha = str_replace(":gutterClick", "#gutterClick", $linha);
                            $linha = str_replace(":copy", "#copy", $linha);
                            $linha = str_replace(":dblclick", "#dblclick", $linha);
                            $linha = str_replace(":touchstart", "#touchstart", $linha);
                            $linha = str_replace(":contextmenu", "#contextmenu", $linha);
                            $linha = str_replace(":viewportChange", "#viewportChange", $linha);
                            $linha = str_replace(":console_submeter", "#console_submeter", $linha);
                            $linha = str_replace(":submeter", "#submeter", $linha);
                            $linha = str_replace(":comando_execucao", "#comando_execucao", $linha);                            

                            $time = explode("#",$linha)[0];
                            list($dia, $mes, $ano, $hor, $min, $seg, $mic) = sscanf($time, '%d/%d/%d@%d:%d:%d:%d');
                            $time_zerofill = $dia."/".$mes."/".$ano.  " "  . sprintf("%02d", $hor) .":". sprintf("%02d", $min) .":". sprintf("%02d", $seg) . "." . $mic;
                            $time_obj = DateTime::createFromFormat("d/m/Y H:i:s.u", $time_zerofill);

                            if ($time_obj) {    

                                $data = explode("#",$linha);
                                array_shift($data);
                                $data = implode("#",$data);
                                $linha = $ano."-".$mes."-".$dia." ".sprintf("%02d", $hor).":".sprintf("%02d", $min).":".sprintf("%02d", $seg).".".sprintf("%03d", $mic)."#".$data;                                

                                if ($time_obj->gettimestamp() < $hora_anterior) {
                                    //echo $dir . "/" . $codigo_fonte->id_trabalho . "_" . $codigo_fonte->id_exercicio . ".log\n";                                    
                                    //echo $linha . "\n";                                      
                                    $repetido = 1;
                                    continue;
                                } else {
                                    $repetido = 0;
                                }

                                $hora_anterior = $time_obj->gettimestamp();

                                if ((strpos($linha, '#testar#') !== false) ||
                                    (strpos($linha, '#console_testar#') !== false) ||
                                    (strpos($linha, 'cshell') !== false)) {
                                    $ignorar = 1;
                                    continue;
                                } else {
                                    $ignorar = 0;
                                }           

                                if ((strpos($linha, '#console_submeter#') !== false) ||
                                    (strpos($linha, '#gutterClick#') !== false) ||
                                    (strpos($linha, '#comando_execucao#') !== false)) {
                                    continue;
                                }                              

                            } else {                         
                                if ($repetido || $ignorar) {
                                    continue;
                                }
                            }

                            // Ignorar linhas com comando_execucao
                            if (strpos($linha, 'comando_execucao') !== false) {
                                continue;
                            }

                            $linha = str_replace("#submeter#", "#submit#", $linha);
                            $linha = str_replace("#encerrar#", "#kill_program#", $linha);

                            $linha = str_replace("Seu código não imprimiu a saída correta. Corrija o código e tente novamente.", "Your code did not produce the correct output. Please, correct your code and try again.", $linha);
                            $linha = str_replace("Parabéns, seu código está correto!", "Congratulations, your code is correct!", $linha);
                            $linha = str_replace("Você está quase conseguindo! Seu código está", "You're almost there! Your code is", $linha);
                            $linha = str_replace("correto, mas se você se esforçar mais conseguirá acertar 100% da questão.", "correct, but if you try harder you'll be able to hit 100% of the question.", $linha);

                            $linha = str_replace("&gt;", ">", $linha);
                            $linha = str_replace("&lt;", "<", $linha);                            

                            if (strlen($linha) > 2) {
                                $newlog .= $linha . "\n";
                            }
                        }

                        $newfile = file_put_contents($this->userspath . $codigo_fonte->id_aluno . "/codemirror/" . $codigo_fonte->id_trabalho . "_" . $codigo_fonte->id_exercicio . ".log", $newlog);

                    }
                }
            }

            for ($i = 0; $i< 10000; $i++) {

                $media_ponderada_listas = $soma_ponderada_listas[$i] / $soma_pesos_listas;

                if ($media_ponderada_listas > 0) {

                    $media_ponderada_avaliacoes = $soma_ponderada_avaliacoes[$i] / $soma_pesos_avaliacoes;
                    $media_parcial = ((10 * $media_ponderada_avaliacoes) + $media_ponderada_listas)/11;

                    if (array_key_exists($i, $this->notas)) {
                        //echo "Nota oficial\n";
                        $media_final = $this->notas[$i];

                    } elseif (array_key_exists($i, $prova_final)) {
                        //echo "Nota codebench com prova\n";
                        $media_final = ((2 * $media_parcial) + $prova_final[$i]) / 3;

                    } else {
                        //echo "Nota codebench sem prova\n";
                        $media_final = $media_parcial;

                    }

                    //echo $nomes_alunos[$i] . ": " . round($media_final,2) . "\n";
                    file_put_contents($this->userspath . $i . "/grades/final_grade.data", round($media_final,2));    
                }
            }
        }
        
        echo "CS1 classes: " . count($total_turmas) . "\n";
        echo "Total number of students: " . count($total_students) . "\n";
        echo "Homework exercises: "  . count($homework_exercises) . "\n";
        echo "Exam exercises: "  . count($exam_exercises) . "\n";
        echo "Codes (developed by students): "  . count($total_codes) . "\n";
        echo "Tests and submissions of codes: "  . count($total_executions) . "\n";
    
    }

    public function actionQuestionario() {

        $this->ipc_classes = "(102,103,105,106,107,108,109,110,111,122,124,125,127,128)";   
        
        $alunos = AlunosTurma::find()
            ->where('id_turma IN ' . $this->ipc_classes)
            ->all();

        foreach ($alunos as $aluno) {

            $user = User::findOne($aluno->id_user);

            $path_csv = 'scripts/data/questionario_demografico_2016.csv';
            $csvfile = fopen($path_csv,"r");
                    
            while (($data = fgetcsv($csvfile, 1000, ",")) !== FALSE) { 

                if (levenshtein($user->email,$data[1])<3) {

                    $questionario = UserQuestionario::find()->where(['id_user'=>$user->id])->one();

                    if (!$questionario) {
                        
                        $questionario = new UserQuestionario;
                        $questionario->id_user = $user->id;
                        $questionario->escola_em = $data[3];
                        $questionario->tipo_escola_em = $data[4];
                        $questionario->turno_em = $data[5];
                        $questionario->ano_conclusao_em = $data[6];
                        $questionario->linguagens = $data[7];
                        $questionario->computador_pessoal = $data[8];
                        $questionario->computador_exclusivo = $data[10];
                        $questionario->internet = $data[9];
                        $questionario->trabalho = $data[11];
                        $questionario->nome_empresa = $data[12];
                        $questionario->trabalho_ano_inicio = $data[13];
                        $questionario->trabalho_ano_fim = $data[14];
                        $questionario->graduacao_anterior = $data[15];
                        $questionario->curso_graduacao_anterior = $data[16];
                        $questionario->universidade_graduacao_anterior = $data[17];
                        $questionario->inicio_graduacao = $data[18];
                        $questionario->termino_graduacao = $data[19];
                        $questionario->estado_civil = $data[20];
                        $questionario->filhos = $data[21];

                        // Opcoes adicionadas posteriormente pelo Leandro
                        $questionario->turno_em = -1;
                        $questionario->primeira_opcao_curso = -1;
                        $questionario->motivo_escolha_curso = -1;
                        $questionario->graduacao_pais = -1;
                        $questionario->ano_nascimento = -1;
                        $questionario->sexo = "-1";                        
                        $questionario->ingles = -1;

                        if (!$questionario->save()) {
                            var_dump($questionario->errors);
                            die();
                        }
                    }
                } 
            }              
        }
    }

    protected function deletaLinhas ($trabalho, $codigo) {

        // Se a linguagem for Python 3, eu tiro as strings dos comandos inputs
        if ($trabalho->id_linguagem == 3) {
        
            // Transforma o código em um array de linhas de código
            $array_codigo = explode("\n",$codigo);

            // Para cada linha de código
            foreach ($array_codigo as $key => $value) {
                $array_codigo[$key] = preg_replace("/input\s*\((?:(?:\s*\"(?:\\\\\"|[^\"]\s*)+\"\s*)|(?:'(?:\\\'|[^'])+'))\)/",'input()', $array_codigo[$key]);
            }

            // Retorna $array_codigo implodido usando \n como conector
            return implode("\n", $array_codigo);
        } else {
            return $codigo;
        }
    } 

    public function actionStats($ano, $semestre) {


        if (($ano == 2016) and ($semestre == 1)) {
            $this->ipc_classes = "(102,103,105,106,107,108,109,110,111)";
        }        
        elseif (($ano == 2016) and ($semestre == 2)) {
            $this->ipc_classes = "(122,124,125,127,128)";
        }    
        else if (($ano == 2017) and ($semestre == 1)) {
            $this->ipc_classes = "(135,136,137,138,139,140,141,142,143,144)";
        }
        elseif (($ano == 2017) and ($semestre == 2)) {
            $this->ipc_classes = "(160,162,163,164,165)";
        }
        elseif (($ano == 2018) and ($semestre == 1)) {
            $this->ipc_classes = "(180,181,183,185,186,187,188,189,190)";
        }        
        elseif (($ano == 2018) and ($semestre == 2)) {
            $this->ipc_classes = "(204,205,206,207,208)";
        }                
        elseif (($ano == 2019) and ($semestre == 1)) {
            $this->ipc_classes = "(220,221,222,223,224,225,226,230,231)";
        } 

        $turmas = Turma::find()
            ->where('id IN ' . $this->ipc_classes)
            ->andWhere('numero_turma NOT LIKE "%teste%"')
            ->andWhere(['status' => Turma::STATUS_ACTIVE])
            ->all();

        foreach ($turmas as $turma) {

            $trabalhos = Trabalho::find() 
                ->where(['id_turma' => $turma->id])
                ->andWhere(['status' => Trabalho::STATUS_ACTIVE])
                ->orderBy('id ASC')
                ->all();

            foreach ($trabalhos as $trabalho) {

                $codigos_fonte = CodigoFonte::find()
                    ->where(['id_trabalho' => $trabalho->id])
                    ->orderBy('id ASC')
                    ->all();

                foreach ($codigos_fonte as $codigo_fonte) {

                    // Logs do Codemirror
                    if (!is_dir($this->userspath . $codigo_fonte->id_aluno . "/codemirror")) {
                        mkdir($this->userspath . $codigo_fonte->id_aluno . "/codemirror");
                    }                     

                    if (file_exists($this->path . $codigo_fonte->id_aluno . "/" . $codigo_fonte->id_trabalho . "_" . $codigo_fonte->id_exercicio . ".log")) {

                        // Diretório, arquivo e linhas do log a ser lido
                        $dir = $this->path . $codigo_fonte->id_aluno;
                        $file = $this->file_get_contents_utf8($dir . "/" . $codigo_fonte->id_trabalho . "_" . $codigo_fonte->id_exercicio . ".log");
                        $linhas = explode("\n",$file);

                        foreach ($linhas as $linha) {
                        }
                    }


                }

            }
                        
        }        
    }
    
    protected function file_get_contents_utf8 ($fn) {
        $content = file_get_contents ($fn);
        return mb_convert_encoding ($content, 'UTF-8',  mb_detect_encoding($content, 'UTF-8, ISO-8859-1', true));
    }
}


