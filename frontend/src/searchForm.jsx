import React from 'react';

class SearchForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            selectedType: undefined,
            selectedSize: undefined,
            selectedGender: undefined,
            selectedAge: undefined,
            selectedLocation: undefined,
            selectedDistance: undefined,
            isGoodWithChildren: undefined,
            isGoodWithDogs: undefined,
            isGoodWithCats: undefined,
        };
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(changeEvent) {
        this.setState({
            [changeEvent.target.name]: changeEvent.target.value
        });
    }

    handleSubmit(event) {
        console.log(this.state)
        event.preventDefault();
    }

    
    render() {
        return (
            <div className="App">
                <form>
                <label>
                        Pick type of animal:
                        <select name="selectedType" value={this.state.selectedType} onChange={this.handleChange}>
                            <option value ="dog">Dog</option>
                            <option value="cat">Cat</option>
                            <option value="rabbit">Rabbit</option>
                        </select>
                    </label>
{/* Change to checkboxes */}
                    <br></br>
                    <label>
                        Size:
                        <select name="selectedSize" value={this.state.selectedSize} onChange={this.handleChange}>
                            <option value ="small">Small</option>
                            <option value="medium">Medium</option>
                            <option value="large">Large</option>
                            <option value="xlarge">Extra Large</option>
                        </select>
                    </label>
{/*  */}
                    <br></br>
                    <label>
                        Gender:
                    </label>
                    <label>
                        <input 
                            type="radio"
                            name="selectedGender"
                            value="female"
                            checked={this.state.selectedGender==="female"}
                            onChange={this.handleChange}
                        />
                    Female
                    </label>
                    <label>
                        <input 
                            type="radio"
                            name="selectedGender"
                            value="male"
                            checked={this.state.selectedGender==="male"}
                            onChange={this.handleChange}
                        />
                    Male
                    </label>
{/* Change to checkboxes */}
                    <br></br>
                    <label>
                        Age:
                        <select name="selectedAge" value={this.state.selectedAge} onChange={this.handleChange}>
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
                            name="isGoodWithChildren"
                            value="true"
                            checked={this.state.isGoodWithChildren==="true"}
                            onChange={this.handleChange}
                        />
                    Required
                    </label>
                    <label>
                        <input 
                            type="radio"
                            name="isGoodWithChildren"
                            value="false"
                            checked={this.state.isGoodWithChildren==="false"}
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
                            name="isGoodWithDogs"
                            value="true"
                            checked={this.state.isGoodWithDogs==="true"}
                            onChange={this.handleChange}
                        />
                    Required
                    </label>
                    <label>
                        <input 
                            type="radio"
                            name="isGoodWithDogs"
                            value="false"
                            checked={this.state.isGoodWithDogs==="false"}
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
                            name="isGoodWithCats"
                            value="true"
                            checked={this.state.isGoodWithCats==="true"}
                            onChange={this.handleChange}
                        />
                    Required
                    </label>
                    <label>
                        <input 
                            type="radio"
                            name="isGoodWithCats"
                            value="false"
                            checked={this.state.isGoodWithCats==="false"}
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
                            name="selectedLocation"
                            onChange={this.handleChange}
                        />
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