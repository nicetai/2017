<?php
/* 功能 上报小程序运行时cpu及内存的时时信息
 * POST:Json {"sessiontime":4989602214, "dev_name":"ABCD1234-bb3c5b4b", "sessionid":"bb3c5b4b7cc8716b579c73bdab629ba0", "info":[{"currenttime":0, "CPU":"Do you understand the feeling of missing someone?"}, {"no":0, "logmsg":"Of source I know."}]}
 * taizhigang  20170418
 */
echo "Time: " . date("Y-m-d H:i:s a") . "<br>";

$PostJson = $GLOBALS['HTTP_RAW_POST_DATA'];
echo "PostG: " . $PostJson. "<br>";

//再把json格式的数据转换成php数组
$jsonToArray = json_decode($PostJson); 
//print_r($jsonToArray);

//要创建/追加的文件
$TxtFileName = "Info/ReportMemoryCpu_" . $jsonToArray->sessiontime . "_" . $jsonToArray->dev_name . ".txt";
if( ($TxtRes=fopen($TxtFileName,"a")) === FALSE){
	echo("Open file: " . $TxtFileName . " fail!");
	fclose ($TxtRes); 
	exit();
}
echo ("Open file: " . $TxtFileName. " sucess!");

//要写文件的内容
print_r($jsonToArray->info) ;
foreach( $jsonToArray->info as $event ){
	#echo __LINE__;
	//$StrConents = $StrConents . $jsonToArray->wid . "#" . $jsonToArray->dev_name . "#" . $event->logmsg . "\n";
	$StrInfo = "time:" . $event->currenttime . "#" . "CPU:" . $event->CPU . "#" . "Vmsize:" . $event->VMSIZE . "#" . "RSS:" . $event->RSS . "\n";
	echo "[__LINE__]" . $StrInfo;
	
	//注意数组中有很多想，每一项都要写入
	if(!fwrite ($TxtRes,$StrInfo)){ 
		echo ("Write file: " . $TxtFileName. " - " . $StrInfo ." fail!");
		fclose($TxtRes);
		exit();
	}
	echo ("Write file: " . $TxtFileName . " - " . $StrInfo ." sucess!");
}

// 替换掉<>，同时对' " \ NULL等字符转义——以免影响WEB展示和Json格式
//暂时注销掉下面一行，上报的数据中不会存在要转义的内容 20170419
////$StrConents = str_replace("<"," ",$StrConents);
////$StrConents = str_replace(">"," ",$StrConents);
// addslashes 会转义 ' " \ NULL 而\' 会影响json解析？
//$StrConents = addslashes($StrConents);
//暂时注销掉下面一行，上报的数据中不会存在要转义的内容 20170419
////$StrConents = addcslashes($StrConents,"\"");


fclose ($TxtRes); 

//记录上面文件的名字，以及时间戳，追加方式写入history文件
//ReportLOG 和 ReportERR 维护同一份history，这里面替换成ReportALL 20170322
//$TxtFileName = str_replace("ReportLOG","ReportALL",$TxtFileName);

//$cmd = "sh report_log_list_set.sh " . $jsonToArray->wid . " " . $TxtFileName . " " . $jsonToArray->sessionid;
//echo $cmd;
//system($cmd) ;

?>
