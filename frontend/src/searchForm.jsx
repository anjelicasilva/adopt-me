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
                    <label>
                    <input type="submit" value="Search" onClick={this.handleSubmit}></input>
                    </label>
                </form>
            </div>
        );
    }
}

export default SearchForm;