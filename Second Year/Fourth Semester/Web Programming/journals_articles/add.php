<?php 
  session_start();

  if ($_SESSION['logged_in'] == 'false') {
    $_SESSION['login'] = 'Log in';
    $_SESSION['message'] = '';
    header("location: index.php");
  }

  $mysqli = new mysqli('localhost', 'root', '', 'examen_model');

  if ($_SERVER['REQUEST_METHOD'] == 'POST') {

    $user = $_SESSION['username'];
    $journalname = $_POST['journalname'];
    $summary = $_POST['summary'];
    $date = 2023;

    $sql_check = "select id from journals where name = '$journalname'";
    $response = mysqli_query($mysqli, $sql_check);
    
    if (mysqli_num_rows($response) == 0){
        $sql_add_journal = "insert into journals (name) values ('$journalname')";
        $response_add_journal = mysqli_query($mysqli, $sql_add_journal);

    }

    $sql_check_2 = "select id from journals where name = '$journalname'";
    $response_get_id = mysqli_query($mysqli, $sql_check_2);
    while($row = mysqli_fetch_array($response_get_id)) $journalid = ''. $row['id'] .'';
    $sql = "INSERT INTO articles (user, journalid, summary, date) " . "VALUES ('$user', '$journalid', '$summary', '$date')";
    if ($mysqli->query($sql) === true) {
        header("location: index.php");
      } else {
        $_SESSION['message'] = 'The project could not be saved to the database!';
      }
    }
?>

<!DOCTYPE html>
<html>

<head>
  <title>Articles</title>
  <link rel="stylesheet" type="text/css" href="main.css">
</head>

<body>

  <div class="login-page">
    <div class="form">

      <form class="register-form" method="POST" action="add.php">

        <div style="margin-bottom: 15px;">
          <?= $_SESSION['message'] ?>
        </div>

        <input type="text" placeholder="journalname" name="journalname" required/>
        <input type="text" placeholder="summary" name="summary" required/>

        <input class="submit" type="submit" name="create" value="Add article">

      </form>

    </div>
  </div>

</body>

</html>