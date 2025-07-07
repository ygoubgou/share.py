from dataclasses import dataclass

@dataclass
class UserInput:
    female: int
    age: float
    age_2: float

    iv009_mod: str
    eduyears_mod: float
    eduyears_mod_2: float
    hhsize: int
    hhsize_2: int
    ch001_: int
    ch001_2: int

    sphus: str
    chronic_mod: int
    bmi: float
    bmi_2: float
    thinc_m: float
    thinc_m_2: float
    hc002_mod: float
    hc002_mod_2: float
    hc012_: int
    mobilityind: int
    maxgrip: int
    smoking: int

    ep005_: str
    eurod: float
    sp002_mod: int
    changement_statut: int

    def convert_to_mlinput(self):
        def safe_startswith(s: str, prefix: str) -> bool:
            return isinstance(s, str) and s.startswith(prefix)

        return MLInput(
            female=bool(self.female),
            age=self.age,
            age_2=self.age_2,

            iv009_big_city=safe_startswith(self.iv009_mod, "1."),
            iv009_suburbs=safe_startswith(self.iv009_mod, "2."),
            iv009_large_town=safe_startswith(self.iv009_mod, "3."),
            iv009_rural=safe_startswith(self.iv009_mod, "5."),

            eduyears_mod=self.eduyears_mod,
            eduyears_mod_2=self.eduyears_mod_2,
            hhsize=self.hhsize,
            hhsize_2=self.hhsize_2,
            ch001_=self.ch001_,
            ch001_2=self.ch001_2,

            sphus_excellent=self.sphus == "5. Excellent",
            sphus_very_good=self.sphus == "4. Very good",
            sphus_fair=self.sphus == "2. Fair",
            sphus_poor=self.sphus == "1. Poor",

            chronic_mod=self.chronic_mod,
            bmi=self.bmi,
            bmi_2=self.bmi_2,
            thinc_m=self.thinc_m,
            thinc_m_2=self.thinc_m_2,
            hc002_mod=self.hc002_mod,
            hc002_mod_2=self.hc002_mod_2,
            hc012_=self.hc012_,
            mobilityind=self.mobilityind,
            maxgrip=self.maxgrip,
            smoking=bool(self.smoking),

            ep005_retired=safe_startswith(self.ep005_, "1."),
            ep005_unemployed=safe_startswith(self.ep005_, "3."),
            ep005_sick=safe_startswith(self.ep005_, "4."),
            ep005_other=safe_startswith(self.ep005_, "97."),

            eurod=self.eurod,
            sp002_mod=self.sp002_mod,
            changement_statut=bool(self.changement_statut),
        )

@dataclass
class MLInput:
    female: bool
    age: float
    age_2: float

    iv009_big_city: bool
    iv009_suburbs: bool
    iv009_large_town: bool
    iv009_rural: bool

    eduyears_mod: float
    eduyears_mod_2: float
    hhsize: int
    hhsize_2: int
    ch001_: int
    ch001_2: int

    sphus_excellent: bool
    sphus_very_good: bool
    sphus_fair: bool
    sphus_poor: bool

    chronic_mod: int
    bmi: float
    bmi_2: float
    thinc_m: float
    thinc_m_2: float
    hc002_mod: float
    hc002_mod_2: float
    hc012_: int
    mobilityind: int
    maxgrip: int
    smoking: bool

    ep005_retired: bool
    ep005_unemployed: bool
    ep005_sick: bool
    ep005_other: bool

    eurod: float
    sp002_mod: int
    changement_statut: bool
