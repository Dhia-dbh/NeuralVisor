import React from "react";
import ph from "./../../../../public/pdp.jpg";
import "./Student_Container.css"
function Student_Container(props) {
  return (
    <div className="container centred colored">
      <div className="row" style={{marginLeft:"2%"}}>
        {" "}
        <h6>Student Name</h6>
      </div>
      <div className="row" style={{marginLeft:"2%"}}>
        <small>21 Jul 2024</small>{" "}
      </div>
      <div className="row" style={{marginLeft:"2%" }}>
        {" "}
        <div className="col"> <img className="Studentpfp"  src={ph}></img></div> <div className="col"><button className="shaped arrow-button top-right-button"></button></div>
      </div>
    </div>
  );
}

export default Student_Container;
