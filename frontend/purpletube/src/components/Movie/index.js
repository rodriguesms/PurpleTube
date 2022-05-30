import React from "react";
import { Star, Clock} from "react-feather";
import "./style.css";
function Movie({ duration }) {
  
  return (
    <div className="movie-card">
        <img src="https://m.media-amazon.com/images/M/MV5BMTk5NjkyNzEwOV5BMl5BanBnXkFtZTcwODc5NDI1MQ@@._V1_SX300.jpg" />
        <div className="movie-info">
          <span>
            <Star size={20} />
            <p>7/10</p>
          </span>
          <span>
            <Clock size={20} />
            <p>{duration}</p>
          </span>
        </div>
     
    </div>
  );
}
export default Movie;
