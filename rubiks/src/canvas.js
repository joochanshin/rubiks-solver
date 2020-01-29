import React from 'react';

class Canvas extends React.Component {
    constructor(props) {
      super(props);
      this.state = { width: 0, height: 0 };
      this.updateWindowDimensions = this.updateWindowDimensions.bind(this);
    }
    componentDidMount() {
        this.updateCanvas();
        this.updateWindowDimensions();
        window.addEventListener('resize', this.updateWindowDimensions);
    }
    componentWillUnmount() {
        window.removeEventListener('resize', this.updateWindowDimensions);
    }

    updateWindowDimensions() {
        this.setState({ width: window.innerWidth, height: window.innerHeight });
    }
    updateCanvas() {
        const ctx = this.refs.canvas.getContext('webgl');
    }
//---------------------------------------------------------------------------------------------
    render() {
        return (
            <canvas ref="canvas" width={window.innerWidth} height={window.innerHeight}/>
        );
    }
}
export default Canvas