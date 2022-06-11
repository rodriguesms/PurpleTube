import React, { useEffect, useState } from "react";
import { Button } from "@material-ui/core";
import Movie from "../../components/Movie";
import { api } from "../../services/api";
import "./style.css";
import { Search } from "react-feather";
import { TopBar } from "../../components/TopBar";

function Home() {
  const [categories, setCategories] = useState();
  const [movies, setMovies] = useState();
  const [value, setValue] = useState();
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    api.get("categories/all").then((response) => {
      setCategories(response.data);
      setLoading(false);
      console.log(categories)
    });
  }, []);

  // useEffect(() => {
  //   api.get("movies/movie_category/Ação").then((response) => {
  //     setMovies(response.data);
  //     console.log(movies);
  //   });
  // }, []);
  // function handleChangeCategory(category) {
  //   api.get(`movies/movie_category/${category}`).then((response) => {
  //     setMovies(response.data);
  //   });
  // }
  // function handleChange(event) {
  //   const { value } = event.target;
  //   setValue(value);
  // }
  // function handleSubmit(event) {
  //   event.preventDefault();
  //   console.log(value);
  //   api.get(`movies/movie_name/${value}`).then((response) => {
  //     setMovies(response.data);
  //     console.log(movies);
  //   });
  // }
  return (
    <div className="homeContainer">
      <div className="top-home">
        <TopBar />
      </div>
      <div className="body-home">
        <div className="navBar">
          {!loading &&
            categories.map((category) => 
              <div onClick={() => console.log(category.nome_categoria)} className="categoryList" key={category.codigo_categoria}>
                {category.nome_categoria}
              </div>
            )
          }
        </div>
        <div className="movieDisplay"></div>
      </div>
    </div>
  );
}
export default Home;
