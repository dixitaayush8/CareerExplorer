import React, { Component } from "react";
import "./Search.css";

class Search extends Component {
  state = {
  searchValue: '',
  keywords: []
  };

  makeApiCall = searchInput => {
  var searchUrl = 'https://careerfinderapi.herokuapp.com/getkeywordrecommendations';
  console.log(searchInput);
  fetch(searchUrl, { headers: {
    'search': searchInput
     }})
  .then(response => {
  return response.json();
  })
  .then(jsonData => {
  this.setState({ keywords: jsonData.keywords });
  });
  };



// fetch(searchUrl, headers: {
//     "Content-Type": "application/json"
//   }).then(response => {
// return response.json();
// })
// .then(jsonData => {
// console.log(jsonData.keyword);
// });
// };

  handleOnChange = event => {
this.setState({ searchValue: event.target.value });
};

handleKeyPress = event => {
  if (event.charCode === 13){
    event.preventDefault();
    this.handleSearch();
  }
}

handleSearch = () => {
  this.makeApiCall(this.state.searchValue);
}

render() {
  return (
  <div>
  <h1>Career Explorer</h1>
  <p>Welcome to Career Explorer! Please enter in some skills in order to explore potential career interest keywords.</p>
  <h1></h1>
  <input
    name="text"
    type="text"
    placeholder="Search"
    onChange={event => this.handleOnChange(event)}
    onKeyPress={event => this.handleKeyPress(event)}
    value={this.state.searchValue}
/>
  <button onClick={this.handleSearch}>Search</button>
  {this.state.keywords ? (
    <div>
    {this.state.keywords.map((keyword, index) => (
    <div key={index}>
    <p>{keyword.keyword}</p>
    </div>
    ))}
    </div>
    ) : (
    <p>Try searching for a keyword</p>
    )}
  </div>
  );
}
}
export default Search;
