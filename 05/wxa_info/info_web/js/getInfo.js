/**
 * Created by taizhigang on 2017/4/17.
 */

window.wxa_debug_config = {
    "get_session":"php/show_log_list.php",
    'get_rt_log':'php/show_log.php',
    'get_rt_err':'php/show_error.php',
    'get_rt_status':'php/show_resource.php',
    'get_history_list':'php/get_reverse_list.php',
    'get_history':'php/get_reverse_item.php',
    'set_resource':"php/set_resource.php"
};
window.wxa_debug_config2 = {
    "get_session":"php/get_sessions.php",
    'get_rt_log':'php/show_log.php',
    'get_rt_err':'php/show_log.php',
    'get_rt_status':'php/rt_status.php',
    'get_history_list':'php/history.php',
    'get_history':'php/get_history.php',
    'set_resource':"php/set.php"

};

window.wxa_Info_config = {
	//"show_memory_cpudevSession_list":"php/show_memory_cpudevSession_list.php",
	"show_memory_cpudevSession_list":"http://wxa.jd.com/wxatest/php/show_memory_cpudevSession_list.php",
    "show_memory_cpuSession_list":"http://wxa.jd.com/wxatest/php/show_memory_cpuSession_list.php",
    'show_memory_cpuInfo':'http://wxa.jd.com/wxatest/php/show_memory_cpuInfo.php'
};

//by taizhigang 20170426
window.wxa_Info_running_status = {
    "dev_name":"",
    'sessiontime':"",
	//从多少行开始
	'count':""
};


var select_data_cpu = [];
var select_data_mem = [];
var data_cpu =[]
var data_mem =[]
var data_line_length
var totalPoints = 100;


function start_realtime_log(){
    //首先先判断一下wid是否合法，否则拉取也没有意义


    //取消之前的定时器

	if(window._rt_Info_worker){
        clearInterval(window._rt_Info_worker)
    }
	//if(window._rt_Infosessiontime_worker){
    //    clearInterval(window._rt_Infosessiontime_worker)
    //}
	


    //清空页面内容
    //$('#rt_log').empty();


	// add by taizhigang 20170426
	window._rt_Info_worker = setInterval(function(){
        //拉取实时Info
		if(window.wxa_Info_running_status.count != ""){
			fetch_Info();
		}

    },1000);

	
	// add by taizhigang 20170426
	//window._rt_Infosessiontime_worker = setInterval(function(){
        //拉取实时dev_name
		//fetch_dev_name();
		// alert("55555555555555-----------------------1");
    //},1000);

}


function fetch_Info(){
        $.get(window.wxa_Info_config.show_memory_cpuInfo + "?sessiontime=" + window.wxa_Info_running_status.sessiontime +  "&dev_name=" + window.wxa_Info_running_status.dev_name + "&count=" + wxa_Info_running_status.count,function(data){
        if(data){
			//alert(data.time)
			var data_line = data.show_info_list;
			window.wxa_Info_running_status.count = data.time;
			
			if(data_line.length != 0){
				data_line_length = data_line.length;
				for(var i=0;i<data_line.length;i++){
					var s = data_line[i];
					
					var re_cpu = /\w+(?=%)/g;
					//正则有点问题啊
					//var re_mem = /\w+(?=K$)/g;
					//var re_mem = /(RSS:)(\w+(?=K))/g;
					var pattern = /(RSS:)(\w+(?=K))/;
					var groups = s.match(pattern);
					var re_mem = groups[2];

					var r_cpu = re_cpu.exec(s); 
					//var r_mem = re_mem.exec(s)/1024; 
					var r_mem = parseInt(re_mem/1024);
					//console.log(r_cpu+"================="+r_mem)
					data_cpu.push(r_cpu);
					data_mem.push(r_mem);
				}
			
				set_cpu_timechart()
				set_mem_timechart()
			}		
        }else{
            alert("获取Info信息异常，请联系管理员检查服务器环境")
        }
    },'json');
}

function fetch_session_time(){
        $.get(window.wxa_Info_config.show_memory_cpuSession_list + "?dev_name=" + window.wxa_Info_running_status.dev_name,function(data){
        if(data){
			//$('#session_list').empty();  
			for(var i =0; i < data.length; i++){
                var s = data[i];
                $('#session_list').append('<option value="'+s+'">'+s+'</option>');
            }
        }else{
            alert("获取sessiontime信息异常，请联系管理员检查服务器环境")
        }
    },'json');
}


function fetch_dev_name(){
        $.get(window.wxa_Info_config.show_memory_cpudevSession_list , function(data){
        if(data){
			//$('#dev_name_list').empty();         
            for(var i =0; i < data.length; i++){
                var s = data[i];
                $('#dev_name_list').append('<option value="'+s+'">'+s+'</option>');
            }
        }else{
            alert("获取dev_name信息异常，请联系管理员检查服务器环境")
        }
    },'json');
}


function getCpuData() {
        if (data_cpu.length > 100)
            data_cpu = data_cpu.slice(data_line_length);
		
        // zip the generated y values with the x values
        select_data_cpu = []	
		for (var i = 0; i < totalPoints; ++i){
			select_data_cpu.push([i, data_cpu[i]])		
		}
        return select_data_cpu;
    }
	
function getMemData() {
        if (data_mem.length > 100)
            data_mem = data_mem.slice(data_line_length);

        // zip the generated y values with the x values
        select_data_mem = []	
		for (var i = 0; i < totalPoints; ++i){
			select_data_mem.push([i, data_mem[i]])		
		}
        return select_data_mem;
    }

function set_cpu_timechart(){

    var updateInterval = 300;

    // setup plot
    var options = {
        series: { shadowSize: 0 }, // drawing is faster without shadows
        lines: {fill: true},
        grid: {borderWidth:0 },
        yaxis: { min: 0, max: 100 },
        colors: ["#ff2424"]
    };
	//getCpuData()
    var plot = $.plot($("#live-chart"), [ getCpuData() ], options);
    function update() {
        plot.setData([ getCpuData() ]);
        // since the axes don't change, we don't need to call plot.setupGrid()
        plot.draw();
        setTimeout(update, updateInterval);
    }

    //update();
}


function set_mem_timechart(){

    var stack = 0, bars = true, lines = false, steps = false;
    
    function plotWithOptions() {
        $.plot($("#bar-chart"), [ getMemData(), ], {
            series: {
                stack: stack,
                lines: { show: lines, fill: true, steps: steps },
                bars: { show: bars, barWidth: 0.8 }
            },
            grid: {
                borderWidth: 0, hoverable: true, color: "#777"
            },
			yaxis: { min: 0, max: 500 },
            colors: ["#ff6c24", "#ff2424"],
            bars: {
                  show: true,
                  lineWidth: 0,
                  fill: true,
                  fillColor: { colors: [ { opacity: 0.9 }, { opacity: 0.8 } ] }
            }
        });
    }

    plotWithOptions();
    
    $(".stackControls input").click(function (e) {
        e.preventDefault();
        stack = $(this).val() == "With stacking" ? true : null;
        plotWithOptions();
    });
    $(".graphControls input").click(function (e) {
        e.preventDefault();
        bars = $(this).val().indexOf("Bars") != -1;
        lines = $(this).val().indexOf("Lines") != -1;
        steps = $(this).val().indexOf("steps") != -1;
        plotWithOptions();
    });
}


$(function(){

	//最好分时间段拉取
	fetch_dev_name();
	
	//绑定设置info字段设置方法
    $('#btn_set_dev').click(function(){
		$('#session_list').empty(); 
		var dev_name = $('#dev_name_list').val();
		//"NaN"
        if (dev_name.toString() == "请选择设备" || dev_name == -1) {
            alert("未设置任何设备信息，设置非法！");
            return false;
        }else{
			//alert(dev_name);
			window.wxa_Info_running_status.dev_name = dev_name;
			//fetch_dev_name();
			fetch_session_time();
			
        }
    });
	
    $('#btn_get_Info').click(function(){
		
		var sessiontime = $('#session_list').val();
        if (sessiontime.toString() == "NaN" ) {
            alert("未设置任何sessiontime信息，设置非法！");
            return false;
        }else{
			//alert(sessiontime);
			window.wxa_Info_running_status.sessiontime = sessiontime;
			//alert($('#rt_log').length)
			fetch_Info();
			
			
        }
    });
	
	//定时发送请求
	start_realtime_log();
	//设定图表
	set_cpu_timechart();
	set_mem_timechart();
});
