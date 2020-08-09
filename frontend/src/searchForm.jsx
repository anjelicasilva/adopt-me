import React from 'react';

class SearchForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            type: undefined,
            small: false,
            medium: false,
            large: false,
            xlarge: false,
            gender: undefined,
            age: undefined,
            location: undefined,
            distance: undefined,
            good_with_children: undefined,
            good_with_dogs: undefined,
            good_with_cats: undefined,
        };
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(changeEvent) {
        const value = changeEvent.target.type === "checkbox" ? changeEvent.target.checked : changeEvent.target.value
        this.setState({
            [changeEvent.target.name]: value
        });
    }

    async handleSubmit(event) {
        event.preventDefault();
        const formData = new FormData(document.getElementById('search-form'));
        let size = [];
        for (let item of ['small', 'medium', 'large', 'xlarge']) {
            if (formData.get(item) === 'on') {
                size.push(item);
                formData.delete(item);
            }
        }
        size = size.join();
        formData.append('size', size)
        let params = new URLSearchParams(formData);
        console.log(params.toString());
        await fetch(
            '/search?'+params)
            .then(resp => resp.json())
            .then(data => {console.log(data)})
    }

    
    render() {
        return (
            <div className="App">
                <form id="search-form">
                <label>
                        Pick type of animal:
                        <select name="type" value={this.state.type} onChange={this.handleChange}>
                            <option value ="dog">Dog</option>
                            <option value="cat">Cat</option>
                            <option value="rabbit">Rabbit</option>
                        </select>
                    </label>
                    <br></br>
                        Size:
                        <label>
                            <input 
                                name="small"
                                type="checkbox"
                                checked={this.state.small} 
                                onChange={this.handleChange} />
                            Small
                        </label>
                        <label>
                            <input 
                                name="medium"
                                type="checkbox"
                                checked={this.state.medium} 
                                onChange={this.handleChange} />
                            Medium
                        </label>
                        <label>
                            <input 
                                name="large"
                                type="checkbox"
                                checked={this.state.large} 
                                onChange={this.handleChange} />
                            Large
                        </label>
                        <label>
                            <input 
                                name="xlarge"
                                type="checkbox"
                                checked={this.state.xlarge} 
                                onChange={this.handleChange} />
                            X-Large
                        </label>
{/*  */}
                    <br></br>
                    <label>
                        Gender:
                    </label>
                    <label>
                        <input 
                            type="radio"
                            name="gender"
                            value="female"
                            checked={this.state.gender==="female"}
                            onChange={this.handleChange}
                        />
                    Female
                    </label>
                    <label>
                        <input 
                            type="radio"
                            name="gender"
                            value="male"
                            checked={this.state.gender==="male"}
                            onChange={this.handleChange}
                        />
                    Male
                    </label>
{/* Change to checkboxes */}
                    <br></br>
                    <label>
                        Age:
                        <select name="age" value={this.state.age} onChange={this.handleChange}>
                            <option value ="baby">Baby</option>
                            <option value="young">Young</option>
                            <option value="adult">Adult</option>
                            <option value="senior">Senior</option>
                        </select>
                    </label>
{/*  */}
                    <br></br>
                    <label>
                        Good with Children:
                    </label>
                    <label>
                        <input 
                            type="radio"
                            name="good_with_children"
                            value="true"
                            checked={this.state.good_with_children==="true"}
                            onChange={this.handleChange}
                        />
                    Required
                    </label>
                    <label>
                        <input 
                            type="radio"
                            name="good_with_children"
                            value="false"
                            checked={this.state.good_with_children==="false"}
                            onChange={this.handleChange}
                        />
                    Not Required
                    </label>
                    <br></br>
                    <label>
                        Good with Dogs:
                    </label>
                    <label>
                        <input 
                            type="radio"
                            name="good_with_dogs"
                            value="true"
                            checked={this.state.good_with_dogs==="true"}
                            onChange={this.handleChange}
                        />
                    Required
                    </label>
                    <label>
                        <input 
                            type="radio"
                            name="good_with_dogs"
                            value="false"
                            checked={this.state.good_with_dogs==="false"}
                            onChange={this.handleChange}
                        />
                    Not Required
                    </label>
                    <br></br>
                    <label>
                        Good with Cats:
                    </label>
                    <label>
                        <input 
                            type="radio"
                            name="good_with_cats"
                            value="true"
                            checked={this.state.good_with_cats==="true"}
                            onChange={this.handleChange}
                        />
                    Required
                    </label>
                    <label>
                        <input 
                            type="radio"
                            name="good_with_cats"
                            value="false"
                            checked={this.state.good_with_cats==="false"}
                            onChange={this.handleChange}
                        />
                    Not Required
                    </label>
                    <br></br>
                    <label>
                        Location:
                    </label>
                    <label>
                        <input
                            type="text"
                            name="location"
                            onChange={this.handleChange}
                        />
                    </label>
                    <br></br>
                    <label>
                        Distance:
                        <select name="distance" value={this.state.distance} onChange={this.handleChange}>
                            <option value ="5">5 miles</option>
                            <option value="10">10 miles</option>
                            <option value="25">25 miles</option>
                            <option value="50">50 miles</option>
                        </select>
                    </label>
                    <br></br>
                    <label>
                    <input type="submit" value="Search" onClick={this.handleSubmit}></input>
                    </label>
                </form>
            </div>
        );
    }
}

export default SearchForm;