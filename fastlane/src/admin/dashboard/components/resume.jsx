import "./resume.css"
function Resume(){
    return(
    <div id="resume">
        <div id="left">
            <h1 id="helloHeading">Hello Maxim,</h1>
            
            <div id="numbers">
                <label className="numberTitle">Today's revenue</label>
                <h2 style={{fontSize:24, margin:0,padding:0, color:"#278C31"}}>3 456.55$</h2>
                <label className="numberTitle">Today's loses</label>
                <h2 style={{fontSize:24, margin:0,padding:0, color:"red"}}>-456.98$</h2>
            </div>
        </div>
        <div id="right">
            <img style={{width:"90%", height:"auto"}} src="/savings.svg"/>
        </div>
        
        
    </div>)
}

export default Resume;