"use client";

type Props = {
  days: number;
  setDays: (value: number) => void;
  hours: number;
  setHours: (value: number) => void;
};

export default function StudySettings({
  days,
  setDays,
  hours,
  setHours,
}: Props) {
  return (
    <div className="bg-white rounded-2xl shadow-md p-8 mt-8 max-w-3xl mx-auto">

      <h2 className="text-2xl font-semibold text-center text-slate-800">
        Study Preferences
      </h2>

      <p className="text-center text-slate-500 mt-2">
        Tell us your study schedule.
      </p>

      <div className="mt-8">

        <label className="block font-medium mb-2">
          Number of Days
        </label>

        <input
          type="number"
          min={1}
          value={days}
          onChange={(e) => setDays(Number(e.target.value))}
          className="w-full border rounded-lg p-3"
        />

      </div>

      <div className="mt-8">

        <label className="block font-medium mb-4">
          Daily Study Hours
        </label>

        <div className="grid grid-cols-4 gap-4">

          {[1,2,3,4].map((h)=>(
            <button
              key={h}
              onClick={()=>setHours(h)}
              className={`rounded-lg p-3 border transition
                ${
                  hours===h
                  ? "bg-blue-600 text-white"
                  : "bg-white hover:bg-slate-100"
                }`}
            >
              {h} {h===4 ? "+" : ""}
            </button>
          ))}

        </div>

      </div>

    </div>
  );
}