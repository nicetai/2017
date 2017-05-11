<?php

//echo "Time: " . date("Y-m-d H:i:s a") . "<br>";
header('Content-type: application/json');
header('Access-Control-Allow-Origin:*');


$path = "/export/webadmin/web/wxatest/php/Info/";

//定义一个函数，查找指定目录下所有的文件，不包括子目录中的文件
function get_file_list($dir){
	$regex = '/([0-9]{10})/';
	$regex1 = '/(_[A-Za-z0-9]+.txt)/';
	$regex2 = '/(?<=[0-9]_).+?(?=.txt)/';
	//$regex = '/'.'[0-9]{10}_'.$dev_name.'/';
    $file_list = array();
	$file_session_list = array();
	$file_dev_list = array();
	$file_session_list_total = array();
//    $file_dir_list = array();
     
    $dir_list = scandir($dir); //查找目录  
     
    foreach ($dir_list as $r)
    {
        if ($r == '.' || $r == '..')  
        {
            continue;
        }
		//if(preg_match($regex,$r,$file_session_list)){
		//	$file_session_list_total[] = $file_session_list[0];
		//}
		if(preg_match($regex2,$r,$file_dev_list)){
			$file_session_list_total[] = $file_dev_list[0];
		}
    }
	//print_r($file_session_list_total);
//	return array_merge($file_list, $file_dir_list); 
	$arr = array_unique($file_session_list_total); 
    return array_values($arr);
}

$file_session_list_total = get_file_list($path);
//print_r($file_list);
//print_r($file_session_list_total);

echo json_encode($file_session_list_total)
?>
