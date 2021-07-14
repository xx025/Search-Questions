str1="\n" +
    "<style>\n" +
    "    .my_serbox {\n" +
    "        width: 260px;\n" +
    "        z-index: 9999;\n" +
    "        opacity: 0.2;\n" +
    "        position: fixed;\n" +
    "        display: block;\n" +
    "        right: 0;\n" +
    "        bottom: 0;\n" +
    "    }\n" +
    "    textarea {\n" +
    "        border: 0;\n" +
    "    }\n" +
    "</style>\n" +
    "<div class=\"my_serbox\">\n" +
    "    <textarea id=\"ans\" style=\"height: 100px;width: 250px;display: inline-block\">单击清空内容:请在姓名和学号框输入正确然后点击发送</textarea>\n" +
    "     <button id=\"send\" style=\"display: inline-block\">send</button>\n" +
    "    <input id=\"address\" placeholder=\"输入目标服务器通信地址\" style=\"display: inline-block;width: 200px\">\n" +
    "    <input type=\"text\" id=\"username\" placeholder=\"请输入姓名\" style=\"width: 80px;\">\n" +
    "    <input type=\"password\" id=\"password\" placeholder=\"请输入学号\" style=\"width: 80px\">\n" +
    "</div>\n" +
    "<script>\n" +
    "    function send_server() {\n" +
    "        $.ajax({\n" +
    "            url: $(\"#address\").val() + 'souti',\n" +
    "            type: \"post\",\n" +
    "            data: JSON.stringify({\n" +
    "                'questext': $(\"#ans\").val(),\n" +
    "                'user': $('#username').val(),\n" +
    "                'pass': $(\"#password\").val()\n" +
    "            }),\n" +
    "            contentType: 'application/json; charset=UTF-8',\n" +
    "            success: function (res) {\n" +
    "                $(\"#ans\").val(res.anstext);\n" +
    "            },\n" +
    "            error: function (res) {\n" +
    "            }\n" +
    "        });\n" +
    "    }\n" +
    "\n" +
    "    //点击输入框清空输入框内容\n" +
    "    $(\"#ans\").click(\n" +
    "        function () {\n" +
    "            $(\"#ans\").val(\"\");\n" +
    "        }\n" +
    "    )\n" +
    "    $(\"#send\").click(\n" +
    "        function () {\n" +
    "            send_server()\n" +
    "        }\n" +
    "    )\n" +
    "    //键盘监听\n" +
    "    $(document).keydown(function (event) {\n" +
    "        if (event.keyCode == 13) {\n" +
    "            send_server();\n" +
    "        }\n" +
    "    });\n" +
    "</script>"

$(".page-body").append(str1);