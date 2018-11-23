import xlwt
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *

# Create your views here.
def export_akun(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="export-akun.xlsx"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # sheet header, first row
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Kode', 'Name', 'Kd Jenis Beli', 'Tahun',]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Akun.objects.all().values_list('kdakun', 'nmakun', 'kdjenbel', 'tahun')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

def export_bulan(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="export-bulan.xlsx"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # sheet header, first row
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Kode', 'Name']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Bulan.objects.all().values_list('kdbulan', 'nmbulan')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

def export_dept(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="export-dept.xlsx"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # sheet header, first row
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Kode', 'Name']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Dept.objects.all().values_list('kddept', 'nmdept')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

def export_fungsi(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="export-fungsi.xlsx"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # sheet header, first row
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Kode', 'Name']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Fungsi.objects.all().values_list('kdfungsi', 'nmfungsi')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


def export_program(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="export-program.xlsx"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # sheet header, first row
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Kd Fungsi', 'Kd Sfungsi', 'Kd Program', 'Name', 'Tahun', 'Versi']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Program.objects.all().values_list('kdfungsi', 'kdsfungsi', 'kdprogram', 'nmprogram', 'tahun', 'versi')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

def export_giat(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="export-giat.xlsx"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # sheet header, first row
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Kd Fungsi', 'Kd Sfungsi', 'Kd Program', 'Kd Giat', 'Name', 'Versi', 'Tahun']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Giat.objects.all().values_list('kdfungsi', 'kdsfungsi', 'kdgiat', 'nmgiat', 'versi', 'tahun')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

def export_unit(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="export-unit.xlsx"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # sheet header, first row
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Kd Dept', 'Kd Unit', 'Name']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Unit.objects.all().values_list('kddept', 'kdunit', 'nmunit')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

def export_kotam(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="export-kotam.xlsx"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # sheet header, first row
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Kd Dept', 'Kd Unit', 'Kd Kotama', 'Nm Kotama', 'Kd Kukotama']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Kotam.objects.all().values_list('kddept', 'kdunit', 'kdkotama', 'nmkotama', 'kdkukotama')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

def export_output(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="export-output.xlsx"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # sheet header, first row
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Kd Fungsi', 'Kd sFungsi', 'Kd Program', 'Kd Giat', 'Kd Output', 'Kd Output1', 'Nm Output']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Output.objects.all().values_list('kdfungsi', 'kdsfungsi', 'kdprogram', 'kdgiat', 'kdoutput', 'kdoutput1', 'nmoutput')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

def export_satkun(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="export-satkun.xlsx"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # sheet header, first row
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Kd Giat', 'Kd Output', 'Kd Akun', 'Kd Sakun', 'Nm Sakun', 'Kd Dipa']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Satkun.objects.all().values_list('kdgiat', 'kdoutput', 'kdakun', 'kdsakun', 'nmsakun', 'kddipa')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

def export_satkur(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="export-satkur.xlsx"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # sheet header, first row
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Kd Dept', 'Kd Unit', 'Kd Kotama', 'Kd SatKR', 'Nm SatKR', 'Kd Kusatker']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Satkr.objects.all().values_list('kddept', 'kdunit', 'kdkotama', 'kdsatkr', 'nmsatkr', 'kdkusatkr')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

def export_subsatkr(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="export-subsatkr.xlsx"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # sheet header, first row
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Kd Dept', 'Kd Unit', 'Kd Kotama', 'Kd SatKR', 'Kd SubSatKR', 'Nm SubSatKR']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Subsatkr.objects.all().values_list('kddept', 'kdunit', 'kdkotama', 'kdsatkr', 'kdsubsatkr', 'nmsubsatkr')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

def export_wasgiat(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="export-wasgiat.xlsx"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # sheet header, first row
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Kd Wasgiat', 'Nama']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Wasgiat.objects.all().values_list('kdwasgiat', 'nmwasgiat')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

def export_tingkat(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="export-tingat.xlsx"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # sheet header, first row
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Kd Tingkat', 'Pengguna', 'Kd Wasgiat']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Tingkat.objects.all().values_list('kdtingkat', 'pengguna', 'kdwasgiat')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

def export_kegiatan(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="export-kegiatan.xlsx"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # sheet header, first row
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Kd Kegiatan', 'Nm Kegiatan', 'Keterangan', 'Budget', 'Status', 'Created by', 'Child ID']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Kegiatan.objects.all().values_list('kdkegiatan', 'nmkegiatan', 'keterangan', 'budget', 'status', 'created_by', 'parent')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

def home(request):
    return render(request, 'for_export.html')