var updater = {
    poll: function(){
        $.ajax({url: "/longpolling", 
                type: "POST", 
                dataType: "text",
                data: "test=xx",
                success: updater.onSuccess,
                error: updater.onError});
    },
    onSuccess: function(data, dataStatus){
        try{
        	// 往<body></body>里写东西(可以立刻输出)
            $("body").append("<p>"+data+"--"+dataStatus+"</p>");
        }
        catch(e){
            updater.onError();
            return;
        }
        interval = window.setTimeout(updater.poll, 0);
    },
    onError: function(){
        console.log("Poll error;");
    }
};