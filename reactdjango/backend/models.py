# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Certificadomedico(models.Model):
    idcertificado_medico = models.AutoField(db_column='idCertificado_medico', primary_key=True)  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha')  # Field name made lowercase.
    cabeza = models.CharField(db_column='Cabeza', max_length=115)  # Field name made lowercase.
    ojos = models.CharField(db_column='Ojos', max_length=115)  # Field name made lowercase.
    orejas = models.CharField(db_column='Orejas', max_length=115)  # Field name made lowercase.
    nariz = models.CharField(db_column='Nariz', max_length=115)  # Field name made lowercase.
    boca = models.CharField(db_column='Boca', max_length=115)  # Field name made lowercase.
    cuello = models.CharField(db_column='Cuello', max_length=115)  # Field name made lowercase.
    torax = models.CharField(db_column='Torax', max_length=115)  # Field name made lowercase.
    corazon = models.CharField(db_column='Corazon', max_length=115)  # Field name made lowercase.
    pulmon = models.CharField(db_column='Pulmon', max_length=115)  # Field name made lowercase.
    abdomen = models.CharField(db_column='Abdomen', max_length=115)  # Field name made lowercase.
    genitourinario = models.CharField(db_column='Genitourinario', max_length=115)  # Field name made lowercase.
    extremidades = models.CharField(db_column='Extremidades', max_length=215)  # Field name made lowercase.
    informe_fonoaudiologia = models.CharField(db_column='Informe_fonoaudiologia', max_length=215)  # Field name made lowercase.
    idtrabajosocial = models.ForeignKey('TrabajoSocial', models.DO_NOTHING, db_column='IdTrabajoSocial')  # Field name made lowercase.
    idmedicoasignado = models.ForeignKey('Medico', models.DO_NOTHING, db_column='idMedicoAsignado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'certificadomedico'


class Fisioterapeuta(models.Model):
    idfisioterapeuta = models.AutoField(db_column='idFisioterapeuta', primary_key=True)  # Field name made lowercase.
    persona_idpersona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='Persona_idPersona')  # Field name made lowercase.
    fisioterapia_idfisioterapia = models.ForeignKey('Fisioterapia', models.DO_NOTHING, db_column='Fisioterapia_idFisioterapia')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fisioterapeuta'


class Fisioterapia(models.Model):
    idfisioterapia = models.AutoField(db_column='idFisioterapia', primary_key=True)  # Field name made lowercase.
    fechaevaluacion = models.CharField(db_column='FechaEvaluacion', max_length=45)  # Field name made lowercase.
    fechainforme = models.CharField(db_column='FechaInforme', max_length=45)  # Field name made lowercase.
    evaluador = models.CharField(db_column='Evaluador', max_length=45)  # Field name made lowercase.
    motivos_informe = models.CharField(db_column='Motivos_informe', max_length=65)  # Field name made lowercase.
    anamnesis = models.CharField(db_column='Anamnesis', max_length=95)  # Field name made lowercase.
    antecedentes_familiares = models.CharField(db_column='Antecedentes_familiares', max_length=105)  # Field name made lowercase.
    antecedentes_personales = models.CharField(db_column='Antecedentes_personales', max_length=105)  # Field name made lowercase.
    examen_fisico_general = models.CharField(db_column='Examen_fisico_general', max_length=95)  # Field name made lowercase.
    diagnostico = models.CharField(db_column='Diagnostico', max_length=85)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=115)  # Field name made lowercase.
    sugerencias = models.CharField(db_column='Sugerencias', max_length=115)  # Field name made lowercase.
    idfisioterapeuta = models.ForeignKey('Personafisioterapia', models.DO_NOTHING, db_column='idFisioterapeuta')  # Field name made lowercase.
    trabajo_social_idtrabajosocial = models.ForeignKey('TrabajoSocial', models.DO_NOTHING, db_column='Trabajo Social_idTrabajoSocial')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'fisioterapia'


class Informepsicologico(models.Model):
    idinformepsicologico = models.AutoField(db_column='idInformePsicologico', primary_key=True)  # Field name made lowercase.
    informepsicologicocol = models.CharField(db_column='InformePsicologicocol', max_length=45, blank=True, null=True)  # Field name made lowercase.
    legalintervencion_idlegalintervencion = models.ForeignKey('Legalintervencion', models.DO_NOTHING, db_column='LegalIntervencion_idLegalIntervencion')  # Field name made lowercase.
    legaevaluacion_idevaluacion = models.ForeignKey('Legaevaluacion', models.DO_NOTHING, db_column='LegaEvaluacion_idEvaluacion')  # Field name made lowercase.
    modelogeneral_idmodelogeneral = models.ForeignKey('Modelogeneral', models.DO_NOTHING, db_column='ModeloGeneral_idModeloGeneral')  # Field name made lowercase.
    trabajo_social_idtrabajosocial = models.ForeignKey('TrabajoSocial', models.DO_NOTHING, db_column='Trabajo Social_idTrabajoSocial')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    paciente_idpaciente = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='Paciente_idPaciente')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'informepsicologico'


class Legaevaluacion(models.Model):
    idevaluacion = models.AutoField(db_column='idEvaluacion', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'legaevaluacion'


class Legalintervencion(models.Model):
    idlegalintervencion = models.AutoField(db_column='idLegalIntervencion', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'legalintervencion'


class Medico(models.Model):
    idmedico = models.AutoField(db_column='idMedico', primary_key=True)  # Field name made lowercase.
    matricula = models.CharField(db_column='Matricula', max_length=45)  # Field name made lowercase.
    persona_idpersona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='Persona_idPersona')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'medico'


class Modelogeneral(models.Model):
    idmodelogeneral = models.AutoField(db_column='idModeloGeneral', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'modelogeneral'


class Paciente(models.Model):
    idpaciente = models.AutoField(db_column='idPaciente', primary_key=True)  # Field name made lowercase.
    idpersona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='idPersona')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'paciente'


class Persona(models.Model):
    idpersona = models.AutoField(db_column='idPersona', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=45)  # Field name made lowercase.
    fechanacimiento = models.CharField(db_column='FechaNacimiento', max_length=45)  # Field name made lowercase.
    gradoinstruccion = models.CharField(db_column='GradoInstruccion', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ci = models.CharField(db_column='CI', max_length=45)  # Field name made lowercase.
    numerotelefono = models.CharField(db_column='NumeroTelefono', max_length=45, blank=True, null=True)  # Field name made lowercase.
    estadocivil = models.CharField(db_column='EstadoCivil', max_length=45)  # Field name made lowercase.
    ocupacion = models.CharField(db_column='Ocupacion', max_length=45)  # Field name made lowercase.
    ingresoseconomicos = models.CharField(db_column='IngresosEconomicos', max_length=45, blank=True, null=True)  # Field name made lowercase.
    lugarnacimiento = models.CharField(db_column='LugarNacimiento', max_length=45)  # Field name made lowercase.
    domicilioactual = models.CharField(db_column='DomicilioActual', max_length=45)  # Field name made lowercase.
    vivienda = models.CharField(db_column='Vivienda', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'persona'


class Personafisioterapia(models.Model):
    idpersonafisioterapia = models.AutoField(db_column='idPersonaFisioterapia', primary_key=True)  # Field name made lowercase.
    persona_idpersona = models.ForeignKey(Persona, models.DO_NOTHING, db_column='Persona_idPersona')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'personafisioterapia'


class Psicologo(models.Model):
    idpsicologo = models.AutoField(db_column='idPsicologo', primary_key=True)  # Field name made lowercase.
    especialidad = models.CharField(db_column='Especialidad', max_length=45)  # Field name made lowercase.
    persona_idpersona = models.ForeignKey(Persona, models.DO_NOTHING, db_column='Persona_idPersona')  # Field name made lowercase.
    informepsicologico_idinformepsicologico = models.ForeignKey(Informepsicologico, models.DO_NOTHING, db_column='InformePsicologico_idInformePsicologico')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'psicologo'


class Relacionfamiliar(models.Model):
    idgrupofamiliar = models.AutoField(db_column='idGrupoFamiliar', primary_key=True)  # Field name made lowercase.
    relacion_familiar = models.CharField(db_column='Relacion_familiar', max_length=55)  # Field name made lowercase.
    trabajo_social_idtrabajosocial = models.ForeignKey('TrabajoSocial', models.DO_NOTHING, db_column='Trabajo Social_idTrabajoSocial')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    persona_idpersona = models.ForeignKey(Persona, models.DO_NOTHING, db_column='Persona_idPersona')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'relacionfamiliar'


class TrabajoSocial(models.Model):
    idtrabajosocial = models.AutoField(db_column='idTrabajoSocial', primary_key=True)  # Field name made lowercase.
    ue = models.CharField(db_column='UE', max_length=56)  # Field name made lowercase.
    tipodiscapacidad = models.CharField(db_column='TipoDiscapacidad', max_length=75)  # Field name made lowercase.
    padre = models.CharField(db_column='Padre', max_length=45)  # Field name made lowercase.
    madre = models.CharField(db_column='Madre', max_length=45)  # Field name made lowercase.
    fechaevaluacion = models.CharField(db_column='FechaEvaluacion', max_length=50)  # Field name made lowercase.
    referencia_caso = models.CharField(db_column='Referencia Caso', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    antecedentes = models.CharField(db_column='Antecedentes', max_length=255)  # Field name made lowercase.
    dinamicafamiliar = models.CharField(db_column='DinamicaFamiliar', max_length=80)  # Field name made lowercase.
    salud = models.CharField(db_column='Salud', max_length=65)  # Field name made lowercase.
    paciente_idpaciente = models.ForeignKey(Paciente, models.DO_NOTHING, db_column='Paciente_idPaciente')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'trabajo social'
