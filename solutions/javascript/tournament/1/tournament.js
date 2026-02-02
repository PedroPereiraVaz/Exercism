//
// This is only a SKELETON file for the 'Tournament' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const tournamentTally = (registros) => {
  let output = "Team                           | MP |  W |  D |  L |  P";
  if (!registros) return output;
  const partidos = [...registros.split("\n")];
  const cla = {};
  for (let partido of partidos) {
    const [team1, team2, res] = partido.split(";");

    cla[team1] ??= { MP: 0, W: 0, D: 0, L: 0, P: 0 };
    cla[team2] ??= { MP: 0, W: 0, D: 0, L: 0, P: 0 };

    cla[team1]["MP"] += 1;
    cla[team2]["MP"] += 1;

    if (res === "win") {
      cla[team1]["W"] += 1;
      cla[team1]["P"] += 3;
      cla[team2]["L"] += 1;
    } else if (res === "loss") {
      cla[team2]["W"] += 1;
      cla[team2]["P"] += 3;
      cla[team1]["L"] += 1;
    } else {
      cla[team1]["D"] += 1;
      cla[team1]["P"] += 1;
      cla[team2]["D"] += 1;
      cla[team2]["P"] += 1;
    }
  }

  const claOrder = Object.entries(cla).map(([nombre, stats]) => ({
    nombre: nombre,
    ...stats,
  }));

  claOrder.sort((a, b) => {
    if (a.P !== b.P) return b.P - a.P;
    return a.nombre.localeCompare(b.nombre);
  });

  for (let team of claOrder) {
    output += `\n${team.nombre.padEnd(31, " ")}|  ${team.MP} |  ${team.W} |  ${
      team.D
    } |  ${team.L} |${String(team.P).padStart(3, " ")}`;
  }
  return output;
};
