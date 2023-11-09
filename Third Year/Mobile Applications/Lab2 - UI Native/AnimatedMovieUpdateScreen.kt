import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Button
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.Text
import androidx.compose.material3.TextField
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.navigation.NavController
import com.example.animateapp.AnimatedMovie
import com.example.animateapp.AnimatedMovieViewModel

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun AnimatedMovieUpdateScreen(
    navController: NavController,
    viewModel: AnimatedMovieViewModel,
    movie: AnimatedMovie
) {
    var updatedName by remember { mutableStateOf(movie.name) }
    var updatedStudio by remember { mutableStateOf(movie.studio) }
    var updatedDescription by remember { mutableStateOf(movie.description) }
    var updatedYear by remember { mutableStateOf(movie.year.toString()) }
    var updatedImage by remember { mutableStateOf(movie.image) }
    var updatedReview by remember { mutableStateOf(movie.review) }

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(16.dp)
    ) {
        Text(
            text = "Update Movie",
            fontSize = 24.sp,
            fontWeight = FontWeight.Bold,
            modifier = Modifier.padding(bottom = 16.dp)
        )

        TextField(
            value = updatedName,
            onValueChange = { updatedName = it },
            label = { Text("Name") },
            modifier = Modifier.padding(8.dp)
        )

        TextField(
            value = updatedStudio,
            onValueChange = { updatedStudio = it },
            label = { Text("Studio") },
            modifier = Modifier.padding(8.dp)
        )

        TextField(
            value = updatedDescription,
            onValueChange = { updatedDescription = it },
            label = { Text("Description") },
            modifier = Modifier.padding(8.dp)
        )

        TextField(
            value = updatedYear,
            onValueChange = { updatedYear = it },
            label = { Text("Year") },
            modifier = Modifier.padding(8.dp)
        )

        TextField(
            value = updatedImage,
            onValueChange = { updatedImage = it },
            label = { Text("Image URL") },
            modifier = Modifier.padding(8.dp)
        )

        TextField(
            value = updatedReview,
            onValueChange = { updatedReview = it },
            label = { Text("Review") },
            modifier = Modifier.padding(8.dp)
        )

        Spacer(modifier = Modifier.weight(1f))

        Button(
            onClick = {
                viewModel.updateAnimatedMovie(
                    AnimatedMovie(
                        id = movie.id,
                        name = updatedName,
                        studio = updatedStudio,
                        description = updatedDescription,
                        year = updatedYear.toIntOrNull() ?: 0,
                        image = updatedImage,
                        review = updatedReview
                    )
                )
                navController.popBackStack()
            },
            modifier = Modifier.padding(8.dp)
        ) {
            Text("Update")
        }

        Button(
            onClick = {
                navController.popBackStack()
            },
            modifier = Modifier.padding(8.dp)
        ) {
            Text("Cancel")
        }
    }
}
