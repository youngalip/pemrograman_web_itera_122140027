import { Tabungan, Storage } from './app.js';

const form = document.getElementById('formTabungan');
const list = document.getElementById('listTabungan');
const totalDisplay = document.getElementById('totalTabungan');

let dataTabungan = Storage.ambilSemua();
let editMode = false;
let editId = null;
let currentPage = 1;
const itemsPerPage = 5;

const updateTotal = () => {
  const total = dataTabungan.reduce((sum, item) => sum + item.jumlah, 0);
  totalDisplay.textContent = `Total: Rp ${total.toLocaleString()}`;
};

const renderPagination = () => {
  let pagination = document.getElementById('pagination');
  if (!pagination) {
    pagination = document.createElement('div');
    pagination.id = 'pagination';
    pagination.className = 'flex justify-center gap-4 mt-4';
    list.parentNode.appendChild(pagination);
  }

  const totalPages = Math.ceil(dataTabungan.length / itemsPerPage);
  pagination.innerHTML = '';

  if (currentPage > 1) {
    const prevBtn = document.createElement('button');
    prevBtn.textContent = 'Previous';
    prevBtn.className = 'bg-yellow-400 px-3 py-1 rounded text-white hover:bg-yellow-500';
    prevBtn.onclick = () => {
      currentPage--;
      render();
    };
    pagination.appendChild(prevBtn);
  }

  if (currentPage < totalPages) {
    const nextBtn = document.createElement('button');
    nextBtn.textContent = 'Next';
    nextBtn.className = 'bg-yellow-400 px-3 py-1 rounded text-white hover:bg-yellow-500';
    nextBtn.onclick = () => {
      currentPage++;
      render();
    };
    pagination.appendChild(nextBtn);
  }
};

const render = () => {
  list.innerHTML = '';

  const halamanData = dataTabungan
    .slice()
    .reverse()
    .slice((currentPage - 1) * itemsPerPage, currentPage * itemsPerPage);

  halamanData.forEach(item => {
    const li = document.createElement('li');
    li.className = 'border-l-4 border-yellow-400 bg-yellow-100 p-3 rounded flex justify-between items-center';
    li.innerHTML = `
      <div>
        <p class="font-semibold text-yellow-700">${item.kegiatan}</p>
        <p>Rp ${item.jumlah} - ${item.catatan} - ${item.tanggal}</p>
      </div>
      <div class="flex gap-2">
        <button data-id="${item.id}" class="edit bg-yellow-500 hover:bg-yellow-600 text-white px-2 py-1 rounded">Edit</button>
        <button data-id="${item.id}" class="hapus bg-red-500 hover:bg-red-600 text-white px-2 py-1 rounded">Hapus</button>
      </div>
    `;
    list.appendChild(li);
  });

  updateTotal();
  renderPagination();
};

form.addEventListener('submit', async e => {
  e.preventDefault();
  const kegiatan = document.getElementById('Kegiatan').value.trim();
  const jumlah = parseInt(document.getElementById('jumlah').value);
  const tanggal = document.getElementById('tanggal').value;
  const catatan = document.getElementById('Catatan').value.trim() || 'Umum';

  if (!kegiatan || isNaN(jumlah) || !tanggal) {
    alert(`Mohon isi semua data dengan benar.`);
    return;
  }

  if (editMode) {
    const index = dataTabungan.findIndex(p => p.id === editId);
    dataTabungan[index] = new Tabungan(editId, kegiatan, jumlah, tanggal, catatan);
    await new Promise(resolve => setTimeout(resolve, 400));
    editMode = false;
    editId = null;
  } else {
    const id = Date.now().toString();
    const tabunganBaru = new Tabungan(id, kegiatan, jumlah, tanggal, catatan);
    dataTabungan.push(tabunganBaru);
  }

  Storage.simpanSemua(dataTabungan);
  currentPage = 1;
  render();
  form.reset();
});

list.addEventListener('click', e => {
  if (e.target.classList.contains('hapus')) {
    const id = e.target.dataset.id;
    dataTabungan = dataTabungan.filter(t => t.id !== id);
    Storage.simpanSemua(dataTabungan);
    render();
  }

  if (e.target.classList.contains('edit')) {
    const id = e.target.dataset.id;
    const data = dataTabungan.find(t => t.id === id);

    document.getElementById('Kegiatan').value = data.nama;
    document.getElementById('jumlah').value = data.jumlah;
    document.getElementById('tanggal').value = data.tanggal;
    document.getElementById('Catatan').value = data.kategori;

    editMode = true;
    editId = id;
  }
});

document.addEventListener('DOMContentLoaded', render);
