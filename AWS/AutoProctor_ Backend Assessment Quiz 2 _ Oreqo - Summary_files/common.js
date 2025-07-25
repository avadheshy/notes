const commonFunction = () => {
    console.log("Common function called");
    // Never ever remove this.
}
window.commonFunction = commonFunction;


// Custom Swal Mixin to be used for all modal popups
function apSwal(swalProps) {
    const swalInstance = Swal.mixin({
        focusConfirm: false,
        focusCancel: false,
        focusDeny: false,
        customClass: {
            icon: "mt-5 mb-0 !border-none",
            title: "!text-base font-semibold leading-6 text-gray-900 mx-0 px-5",
            htmlContainer: "text-sm text-gray-500 mx-0 px-5",
            closeButton: "!shadow-none !focus:outline-none",
            confirmButton: "ap-btn-primary__ta !bg-ap-ta-primary !text-sm w-full sm:h-full m-0", // TODO: remove `!` important, once we have a proper fix for the issue
            cancelButton: "ap-btn-secondary__ta !bg-gray-100 !text-black !text-sm w-full sm:h-full m-0",
            denyButton: "ap-btn-secondary__ta hover:bg-red-800 !text-sm w-full sm:h-full m-0",
            actions: "px-5 w-full sm:!flex-nowrap gap-2",
        },
        didOpen: (popup) => {
            // Handle enableCtasAfter if specified
            const enableCtasAfter = swalProps?.enableCtasAfter;
            if (enableCtasAfter) {
                const buttons = popup.querySelectorAll('.swal2-confirm, .swal2-cancel, .swal2-deny');
                const actionsContainer = popup.querySelector('.swal2-actions');
                
                // Create countdown message element
                const countdownMsg = document.createElement('div');
                countdownMsg.className = 'text-sm text-gray-500 mt-2 text-center w-full';
                actionsContainer.after(countdownMsg);
                
                // Disable all buttons
                buttons.forEach(btn => btn.disabled = true);
                
                let timeLeft = parseInt(enableCtasAfter);
                const updateCountdown = () => {
                    countdownMsg.innerHTML = `You can click in <span class="font-bold">${timeLeft} seconds</span> `;
                    if (timeLeft <= 0) {
                        buttons.forEach(btn => btn.disabled = false);
                        countdownMsg.remove();
                    } else {
                        timeLeft--;
                        setTimeout(updateCountdown, 1000);
                    }
                };
                updateCountdown();
            }
        },
    });
    return swalInstance.fire(swalProps);
}

function convertISOStringToLocalDateTime(
    isoDateString,
    include_seconds = false,
    date_only = false,
    include_year = false
) {
    const monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
    let dateTime;
    try {
        const str2 = isoDateString.replace(" ", "T");
        dateTime = new Date(str2);
    } catch (e) {
        return isoDateString;
    }

    const date = dateTime.getDate();
    const month = monthNames[dateTime.getMonth()];
    let hours = dateTime.getHours();
    const year = dateTime.getFullYear();

    let ampm;
    ampm = hours >= 12 ? "PM" : "AM";

    if (hours > 12) {
        hours = hours - 12;
    }

    let minutes = dateTime.getMinutes();
    if (minutes < 10) {
        minutes = "0" + minutes;
    }

    let formattedDate;
    if (include_seconds) {
        let seconds = dateTime.getSeconds();
        if (seconds < 10) {
            seconds = "0" + seconds;
        }

        if (include_year) {
            formattedDate = date + "-" + month + "  " + year + " " + hours + ":" + minutes + ":" + seconds + " " + ampm;
        } else {
            formattedDate = date + " " + month + " " + hours + ":" + minutes + ":" + seconds + " " + ampm;
        }
    } else if (date_only) {
        const year = dateTime.getFullYear();

        if (include_year) {
            formattedDate = date + " " + month + " " + year;
        } else {
            formattedDate = date + " " + month;
        }
    } else {
        if (include_year) {
            formattedDate = date + "-" + month + "  " + year + " " + hours + ":" + minutes + " " + ampm;
        } else {
            formattedDate = date + "-" + month + "  " + hours + ":" + minutes + " " + ampm;
        }
    }

    return formattedDate;
}

function showToast(message, time, type, icon, divExtraClasses, pExtraClasses) {
    let additionalClasses = "";
    let timeout = time | 5000;
    let positionFromTop = "20px";

    if (type === "success") {
        additionalClasses += "border-r-green-500";
    } else if (type === "error") {
        additionalClasses += "border-r-red-500";
    } else if (type === "warning") {
        additionalClasses += "border-r-yellow-500";
    } else if (type === "info") {
        additionalClasses += "border-r-blue-500";
    } else {
        additionalClasses += "border-r-gray-500";
    }

    const allToast = document.querySelectorAll(".ap-toast");

    if (allToast.length > 0) {
        // the next toast should be below the top one
        const lastToast = allToast[allToast.length - 1];
        const lastToastHeight = lastToast.getBoundingClientRect().height;
        const lastToastPositionFromTop = lastToast.style.top.toString().split("px")[0]; // get the number part

        const newToastTop = Number(lastToastPositionFromTop) + lastToastHeight + 10;

        positionFromTop = newToastTop + "px";
    }

    const toastWrapper = document.createElement("div");
    toastWrapper.classList.add(
        "fixed",
        "right-0",
        "px-5",
        "py-4",
        "right-8",
        "border-r-8",
        "bg-gray-100",
        "drop-shadow-lg",
        "rounded-md",
        "z-50",
        "ap-toast",
        additionalClasses
    );

    toastWrapper.style.top = positionFromTop;

    toastWrapper.innerHTML = "<p class='text-sm'>" + message + "</p>";

    document.querySelector("body").appendChild(toastWrapper);

    const timer = setTimeout(function () {
        document.querySelector("body").removeChild(toastWrapper);
        clearTimeout(timer);
    }, timeout);
}

function secondsToHMS(secs) {
    function z(n) {
        return (n < 10 ? "0" : "") + n;
    }
    var sign = secs < 0 ? "-" : "";
    secs = Math.abs(secs);
    return sign + z((secs / 3600) | 0) + ":" + z(((secs % 3600) / 60) | 0) + ":" + z(secs % 60);
}

async function copyTextToClipboard(text, toastMsg = "Copied to clipboard") {
    try {
        await navigator.clipboard.writeText(text);
        showToast(toastMsg, 2000, "success");
    } catch (err) {
        console.log("Oops, unable to copy");
    }
}

function removeSecondsFromTime(time) {
    return time.split(":").slice(0, 2).join(":");
}

function findNextSiblingWithClassName(element, className) {
    let sibling = element.nextElementSibling;
    while (sibling) {
        if (sibling.classList.contains(className)) {
            return sibling;
        }
        sibling = sibling.nextElementSibling;
    }
    return null;
}

function findPreviousSiblingWithClassName(element, className) {
    let sibling = element.previousElementSibling;
    while (sibling) {
        if (sibling.classList.contains(className)) {
            return sibling;
        }
        sibling = sibling.previousElementSibling;
    }
    return null;
}

function findDescendantWithClassName(element, className) {
    for (let i = 0; i < element.children.length; i++) {
        if (element.children[i].classList.contains(className)) {
            return element.children[i];
        } else {
            const child = findDescendantWithClassName(element.children[i], className);
            if (child) {
                return child;
            }
        }
    }
    return null;
}

function findGrandparentWithClassName(element, className) {
    let parent = element.parentElement;
    while (parent) {
        if (parent.classList.contains(className)) {
            return parent;
        }
        parent = parent.parentElement;
    }
    return null;
}

function restrictFeature(event, tierToUpgradeTo = "Premium") {
    event.preventDefault();

    apSwal({
        title: "Upgrade to " + tierToUpgradeTo,
        text:
                "This feature is only available to " +
                tierToUpgradeTo +
                " plan users, and users with a positive balance. Please upgrade to use this feature.",
            iconHtml: statusIcon("warning"),
            showCancelButton: true,
            confirmButtonText: "Upgrade to " + tierToUpgradeTo,
            cancelButtonText: "Cancel",
        })
        .then((res) => {
            if (res.value) {
                window.location = "/test-admin/billing?mustUpgradeTo=" + tierToUpgradeTo;
            }
        });
}

function testImageUrl(testType) {
    if (testType === "socratease") {
        return "/static/img/main/soc-quiz.png";
    } else if (testType === "google") {
        return "/static/img/main/g-form.svg";
    } else if (testType === "microsoft") {
        return "/static/img/main/m-form.svg";
    } else if (testType === "iframe") {
        return "/static/img/main/your-own-site.svg";
    } else {
        return "";
    }
}

function makePostRequestNew(url, payload, onSuccess, params) {
    let ajaxParams = {
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify(payload),
        headers: { "X-CSRF-Token": csrfToken },
    };

    if (url) {
        ajaxParams["url"] = url;
    }

    // onSuccess can be 'nothing', 'reload', 'redirectToFixedUrl', 'redirectToUrlFromResponse' or 'callback'

    $.ajax(ajaxParams)
        .done(function (response) {
            if (response.status === "success") {
                if (onSuccess === "nothing") {
                    if (response.successMsg) {
                        showToast(response.successMsg, 3000, "success");
                    }
                } else if (onSuccess === "redirectToUrlFromResponse") {
                    if (response.successMsg) {
                        apSwal({ title: "Success", html: response.successMsg, iconHtml: statusIcon("success") })
                            .then(() => {
                                window.location = response.successRedirectURL;
                            });
                    } else {
                        window.location = response.successRedirectURL;
                    }
                } else if (onSuccess === "redirectToFixedUrl") {
                    const successRedirectURL = params.successRedirectURL;
                    if (response.successMsg) {
                        apSwal({ title: "Success", html: response.successMsg, iconHtml: statusIcon("success") })
                            .then(() => {
                                window.location = successRedirectURL;
                            });
                    } else {
                        window.location = successRedirectURL;
                    }
                } else if (onSuccess === "reload") {
                    if (response.successMsg) {
                        apSwal({ title: "Success", html: response.successMsg, iconHtml: statusIcon("success") })
                            .then(() => {
                                window.location.reload();
                            });
                    } else {
                        window.location.reload();
                    }
                } else if (onSuccess === "callback") {
                    const successCallbackFn = params?.successCallbackFn || null;

                    if (successCallbackFn) {
                        const successCallbackArgs = params?.successCallbackArgs || null;

                        if (successCallbackArgs && successCallbackArgs?.length > 0) {
                            let allArgs = {};

                            for (let i = 0; i < successCallbackArgs.length; i++) {
                                if (response[successCallbackArgs[i]]) {
                                    allArgs[successCallbackArgs[i]] = response[successCallbackArgs[i]];
                                } else {
                                    allArgs[successCallbackArgs[i]] = null;
                                }
                            }

                            successCallbackFn(allArgs);
                        } else {
                            successCallbackFn();
                        }
                    } else {
                        console.log("No successCallbackFn provided");
                    }
                } else {
                    window.location = response.successRedirectURL;
                }
            } else if (response.status === "error") {
                apSwal({
                        title: "Something went wrong",
                        html: response.errorMsg || "We weren't able to process this request. Please try again.",
                        iconHtml: statusIcon("error"),
                    })
                    .then(() => {
                        if (params?.errorCb) {
                            const errorCb = params.errorCb;
                            const errorCbArgs = params.errorCbArgs || null;
                            if (errorCbArgs) {
                                errorCb(errorCbArgs);
                            } else {
                                errorCb();
                            }
                        }
                    });
            }
        })
        .fail(function () {
            apSwal({
                    title: "Something went wrong",
                    html: "Some error connecting to the server. Please try again.",
                    iconHtml: statusIcon("error"),
                })
                .then(() => {
                    if (params?.errorCb) {
                        const errorCb = params.errorCb;
                        const errorCbArgs = params.errorCbArgs || null;
                        if (errorCbArgs) {
                            errorCb(errorCbArgs);
                        } else {
                            errorCb();
                        }
                    }
                });
        });
}

window.addEventListener("load", function () {
    $(".date-time-localize, .date-localize, .date-time-year-localize, .date-year-localize").each((ind, elem) => {
        const $elem = $(elem);
        if ($elem.text() && $elem.text() !== "None") {
            const isoDateTime = $elem.text();
            let formattedDateTime;
            if ($elem.hasClass("date-time-localize")) {
                formattedDateTime = convertISOStringToLocalDateTime(isoDateTime);
            } else if ($elem.hasClass("date-localize")) {
                formattedDateTime = convertISOStringToLocalDateTime(isoDateTime, false, true);
            } else if ($elem.hasClass("date-time-year-localize")) {
                formattedDateTime = convertISOStringToLocalDateTime(isoDateTime, false, false, true);
            } else if ($elem.hasClass("date-year-localize")) {
                formattedDateTime = convertISOStringToLocalDateTime(isoDateTime, false, true, true);
            }

            $elem.text(formattedDateTime);
            if ($elem.is("td")) {
                const dateTimeObj = new Date(isoDateTime);
                const dateTimeInMS = dateTimeObj.getTime();
                $elem.attr("data-sort", dateTimeInMS);
            }
        } else {
            $elem.text("-");
            if ($elem.is("td")) {
                $elem.attr("data-sort", "-");
            }
        }

        $elem.show();
    });

    $(".show-date-localize").each((ind, elem) => {
        if ($(elem).text() && $(elem).text() !== "None") {
            const isoDateTime = $(elem).text();
            const formattedDateTime = convertISOStringToLocalDateTime(isoDateTime, false, true);
            $(elem).text(formattedDateTime);
        } else {
            $(elem).text("-");
        }

        $(elem).show();
    });
});

const RETRY_WAIT = [15 * 1000, 10 * 1000, 5 * 1000];

function makePostRequest(url, dataDict, callbackOptions, ajaxOptions) {
    let ajaxParams = { type: "POST", contentType: "application/json", data: JSON.stringify(dataDict) };
    if (ajaxOptions) {
        $.extend(ajaxParams, ajaxOptions);
    }
    if (url) {
        ajaxParams["url"] = url;
    }

    if (!callbackOptions) {
        $.ajax(ajaxParams);
        return null;
    }

    const {
        successCallback,
        errorCallback,
        failCallback,
        successArg,
        errorArg,
        failArg,
        successRedirect,
        alwaysCallback,
        alwaysArg,
    } = callbackOptions;

    $.ajax(ajaxParams)
        .done(function (response) {
            if (response.status === "success") {
                if (successCallback === "reload") {
                    if (response.success_msg !== null) {
                        apSwal({ title: "Success!", html: response.success_msg, iconHtml: statusIcon("success") })
                            .then(() => {
                                location.reload();
                            });
                    } else {
                        location.reload();
                    }
                } else if (successRedirect) {
                    if (response.success_msg !== null) {
                        apSwal({ title: "Success!", html: response.success_msg, iconHtml: statusIcon("success") })
                            .then(() => {
                                window.location = successRedirect;
                            });
                    } else {
                        window.location = successRedirect;
                    }
                } else if (successCallback) {
                    const successAjaxArg = response.success_ajax_args;
                    let allArgs = null;
                    if (successAjaxArg && successArg) {
                        allArgs = Object.assign({}, successAjaxArg, successArg);
                    } else if (successAjaxArg) {
                        allArgs = successAjaxArg;
                    } else if (successArg) {
                        allArgs = successArg;
                    }
                    if (typeof response.success_msg !== "undefined" && response.success_msg !== null) {
                        apSwal({ title: "Success!", html: response.success_msg, iconHtml: statusIcon("success") })
                            .then(() => {
                                if (allArgs) {
                                    successCallback(allArgs);
                                } else {
                                    successCallback();
                                }
                            });
                    } else {
                        if (successArg) {
                            successCallback(allArgs);
                        } else {
                            successCallback();
                        }
                    }
                } else {
                    if (response.success_msg !== null) {
                        apSwal({ title: "Success!", html: response.success_msg, iconHtml: statusIcon("success") })
                            .then(() => {
                                if (alwaysCallback && alwaysArg) {
                                    alwaysCallback(alwaysArg);
                                } else if (alwaysCallback) {
                                    alwaysCallback();
                                }
                            });
                    }
                }
            } else if (response.status === "error") {
                if (response.error_msg !== null) {
                    apSwal({
                            title: "Something went wrong",
                            html: response.error_msg,
                            iconHtml: statusIcon("error"),
                        })
                        .then(() => {
                            if (alwaysCallback && alwaysArg) {
                                alwaysCallback(alwaysArg);
                            } else if (alwaysCallback) {
                                alwaysCallback();
                            }
                        });
                } else {
                    apSwal({
                            title: "Something went wrong",
                            html: "Some unexpected error occurred, please try again later.",
                            iconHtml: statusIcon("error"),
                        })
                        .then(() => {
                            if (alwaysCallback && alwaysArg) {
                                alwaysCallback(alwaysArg);
                            } else if (alwaysCallback) {
                                alwaysCallback();
                            }
                        });
                }
            }
        })
        .fail(function () {
            apSwal({
                    title: "Something went wrong",
                    html: "Some unexpected error occurred, either on the server or while connecting to the server",
                    iconHtml: statusIcon("error"),
                })
                .then(() => {
                    if (alwaysCallback && alwaysArg) {
                        alwaysCallback(alwaysArg);
                    } else if (alwaysCallback) {
                        alwaysCallback();
                    }
                });
        })
        .always((response) => {
            if (!successCallback && !successArg && !("status" in response)) {
                console.log("ldxkv");
                if (alwaysCallback && alwaysArg) {
                    alwaysCallback(alwaysArg);
                } else if (alwaysCallback) {
                    alwaysCallback();
                }
            }
        });
}

function makePostRequestWithRetry(url, dataDict, callbackOptions) {
    makePostRequest(url, dataDict, callbackOptions, { retry: true });
}

function showModalPopup(title, content, id = null, showOkBtn = false, okBtnText = "OK", scaleUp = false) {
    $("#ap-modal").show();
    $(".ap-modal-overlay").removeClass("opacity-0 ease-out duration-200");
    $(".ap-modal-overlay").addClass("ease-in duration-300 opacity-100");
    $(".ap-modal-main").removeClass("ease-out duration-200 opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95");
    if (scaleUp) {
        $(".ap-modal-main").addClass("ease-in duration-300 opacity-100 translate-y-0 sm:scale-150");
    } else {
        $(".ap-modal-main").addClass("ease-in duration-300 opacity-100 translate-y-0 sm:scale-100");
    }
    if (title !== "Excel Test") {
        $(".ap-modal-title").html(title);
    } else {
        $(".ap-modal-title").hide();
    }

    $(".ap-modal-content").html(content);
    if (showOkBtn) {
        $(".popup-ok-btn").show();
        $(".popup-ok-btn-text").html(okBtnText);
    }
    if (id) {
        $("#ap-modal-id").val(id);
    }
}

function hideModalPopup() {
    $(".ap-modal-overlay").addClass("opacity-0 ease-out duration-200");
    $(".ap-modal-overlay").removeClass("ease-in duration-300 opacity-100");
    $(".ap-modal-main").addClass("ease-out duration-200 opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95");
    $(".ap-modal-main").removeClass("ease-in duration-300 opacity-100 translate-y-0 sm:scale-100");
    $(".ap-modal-title").html("");
    $(".ap-modal-content").html("");
    $("#ap-modal").hide();
}

function attachEventListeners(el, events, callback) {
    // events -> ['click', 'mouseover', ...]
    events.forEach((event) => {
        el.addEventListener(event, callback);
    });
}


function validateEmail(emailString) {

    // Checking if the email string is empty or not.
    if (!emailString || emailString === '') {
        return {isValid: false, reason: 'Email cannot be empty'};
    }

    // Checking if email has whitespace in between.
    if (/\s/.test(emailString)) {
        return {isValid: false, reason: 'Email cannot have whitespace'};
    }

    // Checking for dot at the beginning or end.
    const dotAtBeginningOrEnd = /^\.|\.$/;
    if (dotAtBeginningOrEnd.test(emailString)) {
        return {isValid: false, reason: 'Email cannot start or end with a dot'};
    }

    // Checking for consecutive dots.
    const consecutiveDots = /\.\./;
    if (consecutiveDots.test(emailString)) {
        return {isValid: false, reason: 'Email cannot contain consecutive dots'};
    }

    // Checking for dot right before or after @
    const dotBeforeOrAfterAt = /\.@|@\./;
    if (dotBeforeOrAfterAt.test(emailString)) {
        return {isValid: false, reason: 'Email cannot have a dot right before or after the @'};
    }

    // Checking for special characters.
    const specialChars = /[!#$%^&*(),={}\[\];:<>\/\\|?]/;
    if (specialChars.test(emailString)) {
        return {isValid: false, reason: 'Email cannot have special characters'};
    }

    // Checking for valid email format.
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (!emailRegex.test(emailString)) {
        return {isValid: false, reason: 'Invalid email format. Emails must contain "@" and "." and have a valid domain'};
    }

    // Checking. for total number of characketers. It should be <= 100.
    if (emailString.length > 100) {
        return {isValid: false, reason: 'Email cannot have more than 100 characters'};
    }

    return { isValid: true, reason: '' };
}