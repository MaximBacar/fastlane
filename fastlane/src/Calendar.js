const Calendar = () => {
  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        background: "white",
        width: "45%",
        height: 400,
        position: "relative",
        margin: 30,
        padding: 10,
        boxShadow: "0px 8px 24px 0px rgba(0, 0, 0, 0.13)",
      }}
    >
      <div
        style={{
          display: "flex",
          width: "100%",
          height: "15%",
          position: "relative",
        }}
      >
        <div
          style={{
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            position: "relative",
            background: "white",
            color: "black",
            width: "50%",
          }}
        >
          <h1>October</h1>
        </div>
        <div
          style={{
            display: "flex",
            marginLeft: 142,
            width: "25%",
            alignItems: "center",
            justifyContent: "center",
          }}
        >
          <button
            style={{
              borderRadius: 50,
              width: 35,
              height: 35,
              margin: 5,
              background: "#2699E5",
              border: "none",
              color: "white",
            }}
          >
            l
          </button>
          <button
            style={{
              borderRadius: 50,
              width: 35,
              height: 35,
              margin: 5,
              background: "#2699E5",
              border: "none",
              color: "white",
            }}
          >
            r
          </button>
        </div>
      </div>

      <div
        style={{
          top: 10,
          display: "flex",
          background: "red",
          width: "100%",
          height: "82%",
          position: "relative",
          color: "white",
        }}
      ></div>
    </div>
  );
};

export default Calendar;
