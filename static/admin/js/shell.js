var help_html =
"<br/><li>help                 -   Displays this dialog </li>" +
"<li>clear                -   Clear the terminal</li>" +
"<li>stats                -   Display system statistics</li>" +
"<li>exit                 -   Return to the dashboard " +
"<li>backup [file]        -   Generates a copy of a file to app/modules/backup</li>" +
"<li>mk [file]            -   Make a file in any format </li>" +
"<li>rm [file]            -   Remove a file in any format </li>" +
"<li>ls [optional:path]   -   List files in directory </li>" +
"<li>cd [path]            -   Go into directory </li>"

var stats_html =
"<li>Trinity-py build tr4.4 by griimnak</li>"

$(function() {
  $('#submit').bind('click', function() {
    $.getJSON('/admin/shell/submit', {
      shellinput: $('input[name="shellinput"]').val(),
    }, function(data) {
      console.log(data.response);
      if (data.response == "TOGGLE_HELP") {
        $("#results").append(help_html),
        data.response = ''
      }
      if (data.response == "TOGGLE_CLEAR") {
        data.response = '',
        document.getElementById('results').innerHTML = ''
      }
      if (data.response == "TOGGLE_STATS") {
        data.response = '',
        $("#results").append(stats_html)
      }
      $("#results").append('<li>'+data.response+'</li>'),
      document.getElementById('shell-input').value = '',
      document.getElementById("shell-input").focus()
    });
    return false;
  });
});
