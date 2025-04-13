export class Tabungan {
    constructor(id, kegiatan, jumlah, tanggal, catatan) {
        this.id = id;
        this.kegiatan = kegiatan;
        this.jumlah = jumlah;
        this.tanggal = tanggal;
        this.catatan = catatan;
      }      
  }
  
  export const Storage = {
    ambilSemua() {
      const data = localStorage.getItem('tabungan');
      return data ? JSON.parse(data) : [];
    },
  
    simpanSemua(dataTabungan) {
      localStorage.setItem('tabungan', JSON.stringify(dataTabungan));
    }
  };
  