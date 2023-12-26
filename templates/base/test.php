<?php    
    if ($permission != 0 && $permission != 2 && $permission != 3) {
        header('Location: index.php');
        exit; 
    }
    
    $date_from = $_GET['date_from'];
    $date_to = $_GET['date_to'];
    
    $today = date("Y-m-d");
    if ($date_from != "" && $date_to != ""){
        $cond = " WHERE `dt` BETWEEN '".date('Y-m-d', strtotime($date_from))." 00:00:00' AND '".date('Y-m-d', strtotime($date_to))." 23:59:59'";
    } else {
        $cond = " WHERE `dt` = '$today'";
        $date_from = date("d.m.Y");
        $date_to = date("d.m.Y");
    }
    
    // Здесь должен быть ваш код для подключения к базе данных и выполнения запроса к БД.
?>

<script type="text/javascript">
    function setDatePicker(period){
        var to = new Date();
        var from = new Date();
        
        switch(period) {
            case "last_week":
                from.setDate(from.getDate() - 7);
                break;
            case "yesterday":
                from.setDate(from.getDate() - 1);
                to = from;
                break;
            case "today":
                from = to;
                break;
            case "tomorrow":
                from.setDate(from.getDate() + 1);
                to = from;
                break;
        }
        
        $('#date_from').datepicker('setDate', from);
        $('#date_to').datepicker('setDate', to);
        document.forms['main'].submit();
    }
    
    $(document).ready(function(){
        
        $( "#date_from, #date_to" ).datepicker({
            dateFormat: "dd.mm.yy",
            changeYear: true,
            firstDay: 1
        });
        
        $.datepicker.setDefaults($.datepicker.regional['ru']);
        
        $('#date_from').datepicker('setDate', '<?php echo $date_from; ?>');
        $('#date_to').datepicker('setDate', '<?php echo $date_to; ?>');
        
        // Здесь должен быть ваш код для обработки результатов запроса к БД и использования DataTables.
    });
</script>

</head>      
<body>    
    <div class="body" style="width: 95%;" id="all_data">
        <form name="main" method="get" action="report.php">
            <input type='hidden' name='report' value='driversreport'>
            <table width="100%">
            <tr>
            <td>
                <div class="head">
                    С <input class="add" style="width: 80px;" type="text" name="date_from" id="date_from" /> 
                    По <input class="add" style="width: 80px;" type="text" name="date_to" id="date_to" />
                    <input class="buttons" type="submit" value="Показать отчёт"/>
                    <a href="javascript: setDatePicker('last_week');" class="buttons">За последнюю неделю</a>
                    <a href="javascript: setDatePicker('yesterday');" class="buttons">Вчера</a>
                    <a href="javascript: setDatePicker('today');" class="buttons">Сегодня</a>
                    <a href="javascript: setDatePicker('tomorrow');" class="buttons">Завтра</a>
                    <h3 class="head_name">Отчёт по водителям</h3>
                </div>
            </td></tr>
            </table> 
        </form>
        
        <!-- Здесь должен быть ваш HTML код для отображения таблицы и данных -->
    </div>
</body> 
</html>
