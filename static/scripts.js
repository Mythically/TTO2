// let auth_key = "KpgOkCV50nJ4nWrIPEwj5dwT71yRVvWcM7SueADm"
// let my_username = "TheMythh"
// let login = my_username+":"+auth_key+"@"
// let tournamentsUrl = login + "api.challonge.com/v1/tournaments.json"

function show(){
    $("#display").attr("background", "black").remove()
    $.getJSON('/get_tourn').done( function (tournament) {
        for (let i = 0; i < tournament.length; i++) {
            $("body").append(`<p>${tournament[i].id}</p>
                           <br>
                           <p>${tournament[i].name}</p>`)
        }

    });
}
function participants(){
    $.getJSON('/get_participants').done(function (participants) {
        console.log(participants)
        for (let i = participants.length-1; i > -1  ; i--) {
        $("body").append(`<p>${participants[i].name}</p>`)
        }
    })
}
