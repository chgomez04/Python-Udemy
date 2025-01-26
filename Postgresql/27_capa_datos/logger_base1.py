import logging as log

log.basicConfig(level= log.CRITICAL)# DEPENDEINDO DE LA CONFIGURACION QUE SE COLOCA MOSTRARA LOS MENSAJES

if __name__ == '__main__':
    log.debug('Mensaje a nivel debug')
    log.info('Mensaje a nivel info')
    log.warning('mensaje a niel warning')
    log.error('Mensaje a nivel error')
    log.critical('Mensaje a nivel critico')


