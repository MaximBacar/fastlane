import Appointments from "./components/appointments";
import Sidebar from "./components/sidebar";
import Resume from "./components/resume";
import "./dashboard2.css"
function Dashboard(){
    return (
        // <div id="dashboard">
        //     <Sidebar/>
        //     <div id="main">
        //         <div id="content">
        //             <h1>Dashboard</h1>
        //             <div id="data">
        //                 <Resume/>
        //                 <Appointments/>
        //             </div>
        //         </div>
        //     </div>
            
        // </div>

        <div id="dashboard">
            <div id="header">

            </div>
            <div id="main">
                <Sidebar/>
                <div id="content">
                    <div className="rows" id="row1">
                        <h1>Dashboard</h1>
                        <Resume/>
                    </div>
                    <div className="rows" id="row2"></div>
                    <div className="rows" id="row2"></div>
                </div>
            </div>
        </div>
    )
}
export default Dashboard;