$(document).ready(function () {
    if (!$("#id_end_date_time").val()) {
        $("#calculateHour").attr('disabled', true);

    } else {
        $("#calculateHour").click(function () {
            var start = new Date($("#id_start_date_time").val());
            var end = new Date($("#id_end_date_time").val());

            let diffInMilliSeconds = Math.abs(end - start) / 1000;

            const hours = Math.floor(diffInMilliSeconds / 3600) % 24;
            diffInMilliSeconds -= hours * 3600;

            $("#id_total_hours").val(hours);
        });
    }

});