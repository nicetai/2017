<?php
/* ���� ����LOG�б��WEB
 * GET:session=4989602214&dev_name=test11&count=5
 * session��ʼʱ�䣬dev_name�豸��Ϣ��������Ϣ��count�ӵڼ��п�ʼ
 * taizhigang 20170419
 */
//echo "Time: " . date("Y-m-d H:i:s a") . "<br>";

header('Content-type: application/json');
header('Access-Control-Allow-Origin:*');

$sessiontime = $_GET['sessiontime'];
$dev_name = $_GET['dev_name'];
$count = $_GET['count'];

class Emp {  
       public $time = "";  
       public $show_info_list  = array();  
   } 

   $e = new Emp();
$show_info_list = array(
		'code' => 200,  
		'msg' => 'OKOKOK',
		'time' => ''
	);

if( $count == 0 ){
	$count = 1;
}

//�ļ�������ReportMemoryCpu_4989602214_ABCD1234-bb3c5b4b.txt
$file_path = 'Info/ReportMemoryCpu_' . $sessiontime . "_" . $dev_name . ".txt";

if (file_exists($file_path)) {
    //echo "The file $file_path exists";
	//$fp = fopen($file_path,"r");
	//$str = fread($fp,filesize($file_path));
	//echo $str = str_replace("\r\n","<br />",$str);

	//while(!feof($fp))
	//{
		//fgets() Read row by row
	//	$buffer .= fgets($fp);
		//echo $str. "<br />";
	//	echo "$buffer";
	//}
	
	$file_arr = file($file_path);
	
	//for($i=0;$i<count($file_arr);$i++){//���ж�ȡ�ļ�����
		//echo $file_arr[$i]."<br />";
	//}
	
	//���ݲ����������ݶ����оʹӶ����п�ʼ��ȡ��һֱ��ȡ�����µ�����
	for($i=$count;$i<count($file_arr);$i++){//���ж�ȡ�ļ�����
		//echo $file_arr[$i]."<br />";
		//echo gettype($file_arr[$i]);
		$e->show_info_list[] = $file_arr[$i];
	}
	
	//���ؿͻ��˶����ĵڼ�ҳ���»ؿͻ�������Ϳ��Դ����µĿ�ʼ
	//$show_info_list['time'] = count($file_arr);
	$e->time = count($file_arr);
	fclose($fp);
} else {
    echo "The file $file_path does not exist";
}


//echo json_encode($show_info_list)
echo json_encode($e)
#echo "sh show_log_list.sh" . " " . $wid . " " . $count;
//system("sh show_log_list.sh $wid $count");

?>
