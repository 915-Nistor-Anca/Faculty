<?php 
  session_start();

  if ($_SESSION['logged_in'] == 'false') {
    $_SESSION['login'] = 'Log in';
    $_SESSION['message'] = '';
    header("location: index.php");
  }

  if ($_SESSION['selected_document_id'] == '') {
    header("location: index.php");
  }

  $mysqli = new mysqli('localhost', 'root', '', 'examen_model');

  $get_documents = "SELECT * FROM documents WHERE id='" . $_SESSION['selected_document_id'] . "'";

  $response = mysqli_query($mysqli, $get_documents);

  while($row = mysqli_fetch_array($response)){
    $keyword1 = ''. $row['keyword1'] .'';
    $keyword2 = ''. $row['keyword2'] .'';
    $keyword3 = ''. $row['keyword3'] .'';
    $keyword4 = ''. $row['keyword4'] .'';
    $keyword5 = ''. $row['keyword5'] .'';
  }

  if ($_SERVER['REQUEST_METHOD'] == 'POST') {

    $keyword1 = $mysqli->real_escape_string($_POST['keyword1']);
    $keyword2 = $mysqli->real_escape_string($_POST['keyword2']);
    $keyword3 = $mysqli->real_escape_string($_POST['keyword3']);
    $keyword4 = $mysqli->real_escape_string($_POST['keyword4']);
    $keyword5 = $mysqli->real_escape_string($_POST['keyword5']);

    $id = $_SESSION['selected_document_id'];

    $sql = "UPDATE documents SET keyword1 = '$keyword1', keyword2 = '$keyword2', keyword3 = '$keyword3', keyword4 = '$keyword4', keyword5 = '$keyword5' WHERE id = '$id'";

    if ($mysqli->query($sql) === true) {
      $_SESSION['selected_document_id'] = '';
      header("location: index.php");
    } else {
      header("location: update.php");
    }

  }

?>


<!DOCTYPE html>
<html>

<head>
  <title>Documents</title>
  <link rel="stylesheet" type="text/css" href="main.css">
</head>

<body>

  <div class="login-page">
    <div class="form">

      <form class="register-form" method="POST" action="update.php">

        <input type="text" placeholder="keyword1" name="keyword1" value="<?= $keyword1 ?>" required/>
        <input type="text" placeholder="keyword2" name="keyword2" value="<?= $keyword2 ?>" required/>
        <input type="text" placeholder="keyword3" name="keyword3" value="<?= $keyword3 ?>" required/>
        <input type="text" placeholder="keyword4" name="keyword4" value="<?= $keyword4 ?>" required/>
        <input type="text" placeholder="keyword5" name="keyword5" value="<?= $keyword5 ?>" required/>

        <input class="submit" type="submit" name="create" value="Update document">

      </form>

    </div>
  </div>

</body>

</html>