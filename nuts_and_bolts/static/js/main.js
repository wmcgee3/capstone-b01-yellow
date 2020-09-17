function feedDatePosted() {
    var datesPosted = document.getElementsByClassName("feed-date-posted");
    if (typeof (datesPosted) != 'undefined' && datesPosted != null) {
        var i;
        for (i = 0; i < datesPosted.length; i++) {
            datesPosted[i].innerHTML = moment.utc(datesPosted[i].dataset.dateTime).local().fromNow();
        }
    }
}
function feedDateUpdated() {
    var datesUpdated = document.getElementsByClassName("feed-date-updated");
    if (typeof (datesUpdated) != 'undefined' && datesUpdated != null) {
        var i;
        for (i = 0; i < datesUpdated.length; i++) {
            datesUpdated[i].innerHTML = "(Updated " + moment.utc(datesUpdated[i].dataset.dateTime).local().fromNow() + ")";
        }
    }
}
function postDatePosted() {
    var datesPosted = document.getElementsByClassName("post-date-posted");
    if (typeof (datesPosted) != 'undefined' && datesPosted != null) {
        var i;
        for (i = 0; i < datesPosted.length; i++) {
            datesPosted[i].innerHTML = moment.utc(datesPosted[i].dataset.dateTime).local().format("[<span class='d-inline-block'>]MMM D, YYYY[</span>] [<span class='d-inline-block'>][at] h:mm A[</span>]");
        }
    }
}
function postDateUpdated() {
    var datesUpdated = document.getElementsByClassName("post-date-updated");
    if (typeof (datesUpdated) != 'undefined' && datesUpdated != null) {
        var i;
        for (i = 0; i < datesUpdated.length; i++) {
            datesUpdated[i].innerHTML = "<span class='d-inline-block'>(Updated " + moment.utc(datesUpdated[i].dataset.dateTime).local().format("MMM D, YYYY[</span>] [<span class='d-inline-block'>][at] h:mm A )[</span>]");
        }
    }
}

feedDatePosted();
feedDateUpdated();
postDatePosted();
postDateUpdated();
