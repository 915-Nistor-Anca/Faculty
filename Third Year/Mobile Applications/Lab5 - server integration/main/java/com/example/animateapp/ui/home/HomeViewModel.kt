package com.example.animateapp.ui.home

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.animateapp.data.AnimatedMovie
import com.example.animateapp.data.MoviesRepository
import kotlinx.coroutines.flow.SharingStarted
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.map
import kotlinx.coroutines.flow.stateIn

class HomeViewModel(moviesRepository: MoviesRepository) : ViewModel() {

    val homeUiState: StateFlow<HomeUiState> =
        moviesRepository.getAllMoviesStream().map { HomeUiState(it) }
            .stateIn(
                scope = viewModelScope,
                started = SharingStarted.WhileSubscribed(TIMEOUT_MILLIS),
                initialValue = HomeUiState()
            )

    companion object {
        private const val TIMEOUT_MILLIS = 5_000L
    }
}

data class HomeUiState(val animatedMovieList: List<AnimatedMovie> = listOf())