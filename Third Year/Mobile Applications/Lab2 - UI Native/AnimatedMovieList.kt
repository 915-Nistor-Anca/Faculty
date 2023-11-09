package com.example.animateapp
import android.util.Log
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material3.Button
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.navigation.NavController

@Composable
fun AnimatedMovieList(navController: NavController, viewModel: AnimatedMovieViewModel) {
    val animatedMoviesState = viewModel.animated_movies_state
    val movies = animatedMoviesState.value

    Column(
        modifier = Modifier.fillMaxSize(),
    ) {
        Spacer(modifier = Modifier.height(30.dp))

        LazyColumn {
            item {
                Text(
                    text = "List of Animated Movies",
                    modifier = Modifier.padding(16.dp),
                    fontSize = 30.sp
                )
            }
            items(movies) { movie ->
                AnimatedMovieListItem(
                    movie = movie,
                    onItemClick = {
                        Log.d("MovieTitleClicked", "Movie title clicked: ${movie.name}")
                        navController.navigate("movieInformation/${movie.id}")
                    },
                    modifier = Modifier.padding(8.dp),
                )
            }

            item {
                Button(
                    onClick = {
                        navController.navigate("addMovie")
                    },
                    modifier = Modifier.padding(16.dp)
                ) {
                    Text("Add")
                }
            }
        }
    }
}
