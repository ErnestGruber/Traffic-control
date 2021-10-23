from GetData import TakePhase

TakePhase.Post(71040)
data = {
  "start_phase_id": 3,
  "time_start_sync": 1632402791,
  "t_cycle": 96,
  "phases": [
    {
      "id": 1,
      "t_osn": 31,
      "t_prom": 9,
      "t_min": 4,
      "is_hidden": bool(0),
      "directions": [0]
    },
    {
      "id": 2,
      "t_osn": 13,
      "t_prom": 9,
      "t_min": 4,
      "is_hidden": bool(0),
      "directions": [0]
    },
    {
      "id": 3,
      "t_osn": 25,
      "t_prom": 9,
      "t_min": 15,
      "is_hidden": bool(0),
      "directions": [0]
    }
  ]
}
print(GetAll.Get(71040))
print(PostCustomPhase.Post(71040, data))
#p = TakePhase.Post(71033, 1)