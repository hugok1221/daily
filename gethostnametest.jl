function gethostname()
	hostname = Vector{UInt8}(undef, 128)
	ccall((:gethostname, "libc"), Int32, (Ptr{UInt8}, Csize_t),
			hostname, sizeof(hostname))
	hostname[end] = 0;
	return unsafe_string(pointer(hostname))
end
