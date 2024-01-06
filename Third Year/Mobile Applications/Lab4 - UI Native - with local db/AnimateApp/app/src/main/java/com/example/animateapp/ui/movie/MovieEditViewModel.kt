package com.example.animateapp.ui.movie

import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.lifecycle.SavedStateHandle
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.animateapp.data.MoviesRepository
import kotlinx.coroutines.flow.filterNotNull
import kotlinx.coroutines.flow.first
import kotlinx.coroutines.launch

class MovieEditViewModel(
    savedStateHandle: SavedStateHandle,
    private val moviesRepository: MoviesRepository
) : ViewModel() {

    var movieUiState by mutableStateOf(MovieUiState())
        private set

    private val movieId: Int = checkNotNull(savedStateHandle[MovieEditDestination.itemIdArg])

    init {
        viewModelScope.launch {
            movieUiState = moviesRepository.getMovieStream(movieId)
                .filterNotNull()
                .first()
                .toMovieUiState(true)
        }
    }

    suspend fun updateMovie() {
        if (validateInput(movieUiState.movieDetails)) {
            moviesRepository.updateMovie(movieUiState.movieDetails.toMovie())
        }
    }


    fun updateUiState(movieDetails: MovieDetails) {
        movieUiState =
            MovieUiState(movieDetails = movieDetails, isEntryValid = validateInput(movieDetails))
    }

    private fun validateInput(uiState: MovieDetails = movieUiState.movieDetails): Boolean {
        return with(uiState) {
            name.isNotBlank() && studio.isNotBlank() && review.isNotBlank()
        }
    }
}