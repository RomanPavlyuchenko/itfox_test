from multiprocessing import cpu_count

bind = '0.0.0.0:80'
workers = cpu_count() * 2 + 1
