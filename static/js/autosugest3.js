$(document).ready(function () {


    $(function () {

        var availabletag = [
            "Napoklu",
             "murnad",
             "virajpet",
              "madikeri2",
              "somarpet",
             "siddapur",
             "Madikeri",
             "Gonikoppal",
             "Kutta",

        ];

        $("#automplete-1").autocomplete({
            source: availabletag,
            minLength: 3,
        });
        $("#automplete-2").autocomplete({
            source: availabletag,
            minLength: 3,
        });
    });
});