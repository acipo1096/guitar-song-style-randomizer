// Song Randomizer
$(document).ready(function () {
  $("#submit").click(function () {
    $(".alert").css("visibility", "visible");
    fetch("/request/song.json");
    fetch("/guitar")
      .then((response) => response.json())
      .then((data) => {
        let a = JSON.stringify(data[0]);
        let s = JSON.stringify(data[1]);
        let artist = new String();
        let song = new String();
        artist = a.toString().replace(/"/g, "");
        song = s.toString().replace(/"/g, "");
        document.getElementById("artist-name").innerHTML = artist;
        document.getElementById("song-name").innerHTML = song;
        $(".alert").css("visibility", "hidden");
      });
  });
});

// Guitar Style Randomizer
$(document).ready(function () {
  $("#go").click(function () {
    try {
      setInterval(getStyles, 1000);
    } catch (error) {}
  });
});

function getStyles() {
  $(".alert").css("visibility", "visible");
  fetch("/licks/style.json");
  fetch("/guitar-styles")
    .then((response) => response.json())
    .then((data) => {
      let g = JSON.stringify(data[0]);
      let s = JSON.stringify(data[1]);
      let guitarist = new String();
      let style = new String();
      guitarist = g.toString().replace(/"/g, "");
      style = s.toString().replace(/"/g, "");
      document.getElementById("guitarist").innerHTML = guitarist;
      document.getElementById("style").innerHTML = style;
      $(".alert").css("visibility", "hidden");
    });
}
