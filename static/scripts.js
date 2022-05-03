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


function matches2(){
    $.getJSON("/matches").done(function (matches) {
        console.log(matches)
        for (let i = 0; i < matches.length; i++) {
            alert(matches[i]['id'])
            $("body").append(`<p>${matches[i]}</p>`)
        }
    })
}

$("#row").ready(displayTournaments())

function displayTournaments() {
    $.getJSON('/get_tourn').done(function (tournaments) {
    $(".cards").remove()
    for(let i = 0; i < tournaments.length; i++) {
    $(".row").append(`<div class="cards col-xl-3 col-lg-4 col-sm-6">
                            <div class="card">
                                <div id="${tournaments[i]['id']}" class="card-body">
                                    <p>Name: ${tournaments[i]['name']}</p>
                                    <p>Participants: ${tournaments[i]['participants']}</p>
                                    <p>Description: ${tournaments[i]['description']} </p>
                                    <form name="show" method="POST" action="/brackets">
                                    <button name="show" type="submit" value="${tournaments[i]['id']}" class="btn btn-primary">Show brackets</button>
                                    </form>
                                </div>
                            </div>
                          </div>`)
    }
    })
}

function a(){
    // $.getJSON("/brackets").done(function (brackets) {
console.log(titles)
    console.log(rounds)
        $(".brackets").brackets({
            titles: titles,
            rounds: rounds,
            color_title: 'black',
            border_color: '#00F',
            color_player: 'black',
            bg_player: 'white',
            color_player_hover: 'white',
            bg_player_hover: 'blue',
            border_radius_player: '10px',
            border_radius_lines: '10px',
        });
        (jQuery);

    // })
}
