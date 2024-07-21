import React from "react";
import SearchBar from "./SearchBar/SearchBar";
import Graph from "./Graph/Graph";
import Student_Container from "./Student_Container/Student_Container";
import "./Student.css";
function Student() {
  return (
    <div>
      <div className="fluid-countainer centred" style={{ marginLeft: "2%" }}>
        <div style={{ marginTop: "5px" }} className="row">
          <SearchBar></SearchBar>
        </div>
        <div style={{ marginTop: "5px" }} className="row">

          <h4>Class focus</h4>

          <div className="row">
            <h6>sort by: Month</h6>
          </div>
        </div>
        <div className="row-6">
          <Graph></Graph>
        </div>
        <h3>Students Performance :</h3>
        <br></br>
        <div style={{ marginTop: "5px" }} className="row stud" >
          <div className="col">
            <Student_Container></Student_Container>
          </div>
          <div className="col ">
            <Student_Container></Student_Container>
          </div>
        </div>
        <div style={{ marginTop: "5px" }} className="row stud">
          <div className="col">
            <Student_Container></Student_Container>
          </div>
          <div className="col">
            <Student_Container></Student_Container>
          </div>
        </div>
        <div style={{ marginTop: "5px" }} className="row stud">
          <div className="col">
            <Student_Container></Student_Container>
          </div>
          <div className="col">
            <Student_Container></Student_Container>
          </div>
        </div>
        <div style={{ marginTop: "5px" }} className="row stud">
          <div className="col">
            <Student_Container></Student_Container>
          </div>
          <div className="col">
            <Student_Container></Student_Container>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Student;
