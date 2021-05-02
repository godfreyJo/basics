import React from 'react';


// this class component illustrates how to use states

class Interact extends React.Component {

    constructor() {
        super()
        this.state = {
            message: 'Machiegni Wendo!'
        }

    }
    changeMessage() {
        this.setState({ message: 'Thank you for following us'})
    }


    render() {
        return (<div>
            <h1>
            {this.state.message}
        </h1>
        <button onClick={() => this.changeMessage()}>Follow</button>

        </div>
        
        )
    }
}

export default Interact