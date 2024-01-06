package com.example.animateapp.ui.movie

import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.lifecycle.ViewModel
import com.example.animateapp.data.AnimatedMovie
import com.example.animateapp.data.MoviesRepository
import java.text.NumberFormat

class MovieEntryViewModel(private val moviesRepository: MoviesRepository) : ViewModel() {

    var movieUiState by mutableStateOf(MovieUiState())
        private set

    fun updateUiState(movieDetails: MovieDetails) {
        movieUiState =
            MovieUiState(movieDetails = movieDetails, isEntryValid = validateInput(movieDetails))
    }

    suspend fun saveItem() {
        if (validateInput()) {
            moviesRepository.insertMovie(movieUiState.movieDetails.toMovie())
        }
    }

    private fun validateInput(uiState: MovieDetails = movieUiState.movieDetails): Boolean {
        return with(uiState) {
            name.isNotBlank() && studio.isNotBlank() && review.isNotBlank()
        }
    }
}

data class MovieUiState(
    val movieDetails: MovieDetails = MovieDetails(),
    val isEntryValid: Boolean = false
)

data class MovieDetails(
    val id: Int = 0,
    val name: String = "",
    val studio: String = "",
    val year: String = "",
    val review: String = ""
)

fun MovieDetails.toMovie(): AnimatedMovie = AnimatedMovie(
    id = id,
    name = name,
    studio = studio,
    year = year.toIntOrNull() ?: 0,
    review = review
)

fun AnimatedMovie.formatedPrice(): String {
    return NumberFormat.getCurrencyInstance().format(studio)
}

fun AnimatedMovie.toMovieUiState(isEntryValid: Boolean = false): MovieUiState = MovieUiState(
    movieDetails = this.toMovieDetails(),
    isEntryValid = isEntryValid
)

fun AnimatedMovie.toMovieDetails(): MovieDetails = MovieDetails(
    id = id,
    name = name,
    studio = studio,
    year = year.toString(),
    review = review
)