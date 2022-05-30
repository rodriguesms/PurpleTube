import React from "react";
import "./style.css";
function Category({ category }) {
  return (
    <button className="container-button">
      <p>{category}</p>
    </button>
  );
}
export default Category;
