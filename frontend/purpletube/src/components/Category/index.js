import { Button } from "@material-ui/core";
import React from "react";
import "./style.css";
function Category({ category }) {
  return (
    <Button className="container-button">
      <p>{category}</p>
    </Button>
  );
}
export default Category;
