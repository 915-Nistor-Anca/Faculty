<?php
    session_start(); 
    
    $mysqli = new mysqli('localhost', 'root', '', 'examen_model');

    $username = $_SESSION['username'];
    $filtered_name = $_SESSION['filtered_name'];

    $sql_get_id_of_the_city = "SELECT id from city where name = '$filtered_name'";
    $response_id = mysqli_query($mysqli, $sql_get_id_of_the_city);

    if (mysqli_num_rows($response_id) > 0){
    while($row = mysqli_fetch_array($response_id)) $cityid = ''. $row['id'] .'';

    $sql = "SELECT * from link where idcity1 = '$cityid' or idcity2 = '$cityid'";
    $response = mysqli_query($mysqli, $sql);
    }
    else {
        echo "This city does not appear in the table.";
    }

?>


<!DOCTYPE html>
<html>
    <body>
    <center>
        <div id="main">
            <h1> Links for selected city </h1>
            <?php
                if (mysqli_num_rows($response_id) > 0 && mysqli_num_rows($response) > 0) {

                    while($row = mysqli_fetch_array($response)){
                        $duration = ''. $row['duration'] .'';
                        $distance = ''. $row['distance'] .'';

                        $id1 = ''. $row['idcity1'] .'';
                        $id2 = ''. $row['idcity2'] .'';
                        $name_city1_sql = "SELECT name from city where id = '$id1'";
                        $name_city2_sql = "SELECT name from city where id = '$id2'";

                        $r1 =mysqli_query($mysqli, $name_city1_sql);
                        $r2 =mysqli_query($mysqli, $name_city2_sql);

                        while($row = mysqli_fetch_array($r1)) $name_city1 = ''. $row['name'] .'';
                        while($row = mysqli_fetch_array($r2)) $name_city2 = ''. $row['name'] .'';
                    
            
                        echo '<div style="margin-bottom: 160px; border-top: 1px solid #ddd;">';
                        echo '<b><h2 style="margin-left: 20px; margin-right: 20px;">'. $name_city1 .', '. $name_city2 .'</h2></b>';
                        echo '<h4 style="margin-left: 20px; text-align: left; text-indent: 50px;">'. $duration .', '. $distance .'</h4>';
                        
                        echo '</div>';
                        
                    }
            
                } else {
                    echo "No links for this city.";
                }
            ?>
        </div>
    </center>
    </body>
</html>