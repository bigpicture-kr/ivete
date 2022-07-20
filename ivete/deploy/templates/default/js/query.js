function query(args) {
    $.ajax({
        url: "/api",
        method: "POST",
        contentType: "application/json",
        data: {'query': JSON.stringify(args.data)},
        success: args.success,
        error: args.error,
    });
}
