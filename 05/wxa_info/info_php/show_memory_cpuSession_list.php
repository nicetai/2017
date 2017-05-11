<?php
/* 功能 返回session及时间列表给WEB
 * GET:dev_name=ABCD1234-bb3c5b4b
 * dev_name纬度，正则匹配返回所有匹配道德session内容
 * taizhigang 20170423
 */

//echo "Time: " . date("Y-m-d H:i:s a") . "<br>";

header('Content-type: application/json');
header('Access-Control-Allow-Origin:*');

$path = "/export/webadmin/web/wxatest/php/Info/";

$dev_name = $_GET['dev_name'];
//$count = $_GET['count'];

//echo $dev_name."----------------";
if(!$dev_name){
	echo "dev_name  error";
}



//定义一个函数，查找指定目录下所有的文件，不包括子目录中的文件
function get_file_list($dir){
	//$regex = '/([0-9]{10})/';
	global $dev_name;
	$regex = '/'.'[0-9]{10}_'.$dev_name.'/';
	$regex2 = '/(?<=[0-9]_).+?(?=.txt)/';
	
	//正则这里还是有问题，会匹配出来和dev_name不匹配的数据,
	//哦，上面问题解决了，PHP的函数里和函数外的坑多注意啊，变量是不一样的
	$regex1 = '/'.'(?<=u_).+?(?=_'.$dev_name.')/';
    $file_list = array();
	$file_session_list = array();
	$file_session_list_total = array();
//    $file_dir_list = array();
     
    $dir_list = scandir($dir); //查找目录  
     
    foreach ($dir_list as $r)
    {
        if ($r == '.' || $r == '..')  
        {
            continue;
        }
		//echo $r . "<br>";
//        $new_dir = $dir . '/' . $r;
//        if (is_dir($new_dir))
//        {
//            $file_dir = get_file_list($new_dir);
//            $file_dir_list = array_merge($file_dir_list, $file_dir);
//        }
//        else
//        {
//            $file_list[] = $new_dir;
//        }
		if(preg_match($regex1,$r,$file_session_list)){
			//echo $r . "<br>";
			$file_session_list_total[] = $file_session_list[0];
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
