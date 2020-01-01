import React, { Component } from "react";
import axios from 'axios';
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

handleSearch = () => {
  this.makeApiCall(this.state.searchValue);
}

render() {
  return (
  <div>
  <h1>Welcome to the keyword search app</h1>
  <input
    name="text"
    type="text"
    placeholder="Search"
    onChange={event => this.handleOnChange(event)}
    value={this.state.searchValue}
/>
  <button onClick={this.handleSearch}>Search</button>
  {this.state.keywords ? (
<div>
{this.state.keywords.map((keyword, index) => (
<div key={index}>
<h1>{keyword.keyword}</h1>
</div>
))}
</div>
) : (
<p>Try searching for a meal</p>
)}
  </div>
  );
}
}
export default Search;
