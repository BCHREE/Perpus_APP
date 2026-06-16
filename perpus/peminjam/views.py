from django.shortcuts import render, redirect

# ==========================================
# DATA STORAGE (VARIABEL GLOBAL MOCKUP DATA)
# ==========================================
DATA_BUKU = [
    {'id': 1, 'judul': 'Laskar Pelangi', 'pengarang': 'Andrea Hirata', 'kategori': 'Novel', 'penerbit': 'Bentang Pustaka', 'tahun': '2005', 'rak': 'A1', 'stok': 5},
    {'id': 2, 'judul': 'Bumi', 'pengarang': 'Tere Liye', 'kategori': 'Fiksi', 'penerbit': 'Gramedia', 'tahun': '2014', 'rak': 'B3', 'stok': 7},
]

DATA_USER = [
    {'id': 1, 'nama': 'Roni Wijaya', 'nis': '220101', 'kelas': 'XI IPA 1', 'kontak': '081234567890'},
    {'id': 2, 'nama': 'Sinta Permata', 'nis': '220102', 'kelas': 'XI IPS 2', 'kontak': '081298765432'},
]

DATA_PEMINJAMAN = [
    {'id': 1, 'nama_siswa': 'Roni Wijaya', 'judul_buku': 'Laskar Pelangi', 'tanggal_pinjam': '2026-06-01', 'tanggal_kembali': '2026-06-08', 'status': 'Dipinjam'},
    {'id': 2, 'nama_siswa': 'Sinta Permata', 'judul_buku': 'Bumi', 'tanggal_pinjam': '2026-06-02', 'tanggal_kembali': '2026-06-09', 'status': 'Dipinjam'},
]


# ==========================================
# 1. FUNGSI VIEW DASHBOARD UTAMA
# ==========================================
def halaman_dashboard(request):
    total_judul = len(DATA_BUKU)
    total_user = len(DATA_USER)
    
    total_buku_awal = 0
    for buku in DATA_BUKU:
        total_buku_awal += int(buku['stok'])
        
    buku_terpinjam = 0
    for pinjam in DATA_PEMINJAMAN:
        if pinjam['status'] == 'Dipinjam':
            buku_terpinjam += 1
            
    total_buku_sekarang = total_buku_awal - buku_terpinjam
    
    # Hitung Sisa Stok Real-Time per Buku untuk Tabel Monitoring Dashboard
    list_buku_dashboard = []
    for buku in DATA_BUKU:
        berapa_kali_dipinjam = 0
        for pinjam in DATA_PEMINJAMAN:
            if pinjam['judul_buku'] == buku['judul'] and pinjam['status'] == 'Dipinjam':
                berapa_kali_dipinjam += 1
        
        sisa_stok = int(buku['stok']) - berapa_kali_dipinjam
        list_buku_dashboard.append({
            'judul': buku['judul'],
            'sisa_stok': sisa_stok
        })

    context = {
        'total_buku': total_buku_sekarang,
        'total_judul': total_judul,
        'total_user': total_user,
        'sedang_dipinjam': buku_terpinjam,
        'sudah_dikembalikan': 0,
        'semua_buku_dashboard': list_buku_dashboard,
    }
    return render(request, 'home.html', context)


# ==========================================
# 2. FUNGSI VIEW KELOLA MASTER BUKU
# ==========================================
def daftar_buku(request):
    return render(request, 'daftar_buku.html', {'semua_buku': DATA_BUKU})

def halaman_tambah_buku(request):
    if request.method == 'POST':
        baru_id = max([buku['id'] for buku in DATA_BUKU]) + 1 if DATA_BUKU else 1
        DATA_BUKU.append({
            'id': baru_id,
            'judul': request.POST.get('judul'),
            'pengarang': request.POST.get('pengarang'),
            'kategori': request.POST.get('kategori'),
            'penerbit': request.POST.get('penerbit'),
            'tahun': request.POST.get('tahun'),
            'rak': request.POST.get('rak'),
            'stok': int(request.POST.get('stok', 0)),
        })
        return redirect('/buku/')
    return render(request, 'tambah_buku.html')

def halaman_edit_buku(request):
    buku_id = int(request.GET.get('id', 0))
    buku_dipilih = None
    for buku in DATA_BUKU:
        if buku['id'] == buku_id:
            buku_dipilih = buku
            break

    if request.method == 'POST' and buku_dipilih:
        buku_dipilih['judul'] = request.POST.get('judul')
        buku_dipilih['pengarang'] = request.POST.get('pengarang')
        buku_dipilih['kategori'] = request.POST.get('kategori')
        buku_dipilih['penerbit'] = request.POST.get('penerbit')
        buku_dipilih['tahun'] = request.POST.get('tahun')
        buku_dipilih['rak'] = request.POST.get('rak')
        buku_dipilih['stok'] = int(request.POST.get('stok', 0))
        return redirect('/buku/')
    return render(request, 'edit_buku.html', {'buku': buku_dipilih})

def halaman_hapus_buku(request):
    buku_id = int(request.GET.get('id', 0))
    for i, buku in enumerate(DATA_BUKU):
        if buku['id'] == buku_id:
            DATA_BUKU.pop(i)
            break
    return redirect('/buku/')


# ==========================================
# 3. FUNGSI VIEW KELOLA ANGGOTA / USER
# ==========================================
def halaman_daftar(request):
    return render(request, 'daftar_user.html', {'semua_user': DATA_USER})

def halaman_tambah_user(request):
    if request.method == 'POST':
        baru_id = max([user['id'] for user in DATA_USER]) + 1 if DATA_USER else 1
        DATA_USER.append({
            'id': baru_id,
            'nama': request.POST.get('nama'),
            'nis': request.POST.get('nis'),
            'kelas': request.POST.get('kelas'),
            'kontak': request.POST.get('kontak'),
        })
        return redirect('/user/')
    return render(request, 'tambah_user.html')

def halaman_detail_user(request):
    user_id = int(request.GET.get('id', 0))
    user_dipilih = None
    for user in DATA_USER:
        if user['id'] == user_id:
            user_dipilih = user
            break
    return render(request, 'detail_user.html', {'user': user_dipilih})

def halaman_edit_user(request):
    user_id = int(request.GET.get('id', 0))
    user_dipilih = None
    for user in DATA_USER:
        if user['id'] == user_id:
            user_dipilih = user
            break

    if request.method == 'POST' and user_dipilih:
        user_dipilih['nama'] = request.POST.get('nama')
        user_dipilih['nis'] = request.POST.get('nis')
        user_dipilih['kelas'] = request.POST.get('kelas')
        user_dipilih['kontak'] = request.POST.get('kontak')
        return redirect('/user/')
    return render(request, 'edit_user.html', {'user': user_dipilih})

def halaman_hapus_user(request):
    user_id = int(request.GET.get('id', 0))
    for i, user in enumerate(DATA_USER):
        if user['id'] == user_id:
            DATA_USER.pop(i)
            break
    return redirect('/user/')


# ==========================================
# 4. FUNGSI VIEW TRANSAKSI PEMINJAMAN
# ==========================================
def daftar_peminjaman(request):
    return render(request, 'daftar_pinjam.html', {'semua_pinjaman': DATA_PEMINJAMAN})

def halaman_pinjam_buku(request):
    if request.method == "POST":
        baru_id = max([p['id'] for p in DATA_PEMINJAMAN]) + 1 if DATA_PEMINJAMAN else 1
        
        nama_siswa = request.POST.get('nama_siswa')
        judul_buku = request.POST.get('judul_buku')
        tgl_pinjam = request.POST.get('tanggal_pinjam')
        tgl_kembali = request.POST.get('tanggal_kembali')
        
        DATA_PEMINJAMAN.append({
            'id': baru_id,
            'nama_siswa': nama_siswa,
            'judul_buku': judul_buku,
            'tanggal_pinjam': tgl_pinjam,
            'tanggal_kembali': tgl_kembali,
            'status': 'Dipinjam'
        })
        return redirect('/peminjaman/')
        
    # Mengirimkan DATA_USER dan DATA_BUKU mockup agar dropdown terisi otomatis
    context = {
        'semua_user': DATA_USER,
        'semua_buku': DATA_BUKU,
    }
    return render(request, 'tambah_pinjam.html', context)